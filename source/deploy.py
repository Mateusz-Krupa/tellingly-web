#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut aus der gewaehlten Fassung den fertigen Deploy-Ordner `dist/`.

Fuenf echte Sprach-URLs statt einer Datei mit ?lang=: jede Sprache bekommt
ihre eigene Adresse, ihren eigenen Titel und ihren vollstaendig vorgerenderten
Text. Damit ist die Seite ohne JavaScript in fuenf Sprachen lesbar, und
Suchmaschinen bekommen fuenf Dokumente statt eines mit fuenf Gesichtern.

Dazu: eigene Schriften statt Google Fonts, Favicon, Vorschaubilder,
robots.txt, Sitemap, Impressum und Datenschutz.
"""
import re, json, pathlib, shutil, datetime

ROOT = pathlib.Path(__file__).resolve().parent
if ROOT.name == "source":
    ROOT = ROOT.parent
DIST = ROOT / "dist"
SITE = "https://tellingly.ch"
LANGS = ["de", "fr", "it", "en"]
HOME = {"de": "/", "fr": "/fr/", "it": "/it/", "en": "/en/"}

src = (ROOT / "versions" / "bold" / "index.html").read_text(encoding="utf-8")

# ------------------------------------------------------------------ I18N lesen
_i = src.index("var I18N={")
_j = src.index("};", _i)
_raw = re.sub(r'^(\s*)([a-z]{2}):\{', r'\1"\2":{', src[_i + len("var I18N="):_j + 1], flags=re.M)
I18N = json.loads(_raw)
assert set(I18N) == set(LANGS), sorted(set(I18N) ^ set(LANGS))

# ------------------------------------------------------------------ 1. Schriften
# Google Fonts raus: das war eine Verbindung zu einem US-Server bei jedem
# Seitenaufruf. Die Schriften liegen jetzt auf demselben Host wie die Seite.
FONTLINKS = re.search(
    r'<link rel="preconnect" href="https://fonts\.googleapis\.com">.*?'
    r'<link href="https://fonts\.googleapis\.com/css2[^>]*>', src, re.S)
assert FONTLINKS, "Google-Fonts-Block nicht gefunden"
LOCALFONTS = (
    '<link rel="preload" href="/fonts/source-serif-4-300-normal-latin.woff2" as="font" type="font/woff2" crossorigin>\n'
    '<link rel="preload" href="/fonts/ibm-plex-mono-400-normal-latin.woff2" as="font" type="font/woff2" crossorigin>\n'
    '<link rel="stylesheet" href="/fonts.css">'
)
src = src.replace(FONTLINKS.group(0), LOCALFONTS, 1)

# ------------------------------------------------------------------ 2. Kopfdaten
# Alle bisherigen Kanonisch-, hreflang- und OG-Zeilen fliegen raus; sie werden
# pro Sprache neu gesetzt, weil jede Sprache jetzt ihre eigene Adresse hat.
src = re.sub(r'\n<link rel="canonical"[^>]*>', "", src)
src = re.sub(r'\n<link rel="alternate" hreflang="[^"]*"[^>]*>', "", src)
src = re.sub(r'\n<meta property="og:(title|description|url)"[^>]*>', "", src)

ICONS = (
    '<link rel="icon" href="/favicon.ico" sizes="32x32">\n'
    '<link rel="icon" href="/favicon.svg" type="image/svg+xml">\n'
    '<link rel="apple-touch-icon" href="/apple-touch-icon.png">\n'
    '<link rel="manifest" href="/site.webmanifest">'
)
src = src.replace('<meta property="og:type" content="website">',
                  ICONS + '\n<meta property="og:type" content="website">', 1)

# ------------------------------------------------------------------ 3. Sprachwahl
# Aus den Knöpfen werden Links auf echte Adressen: ohne JavaScript benutzbar,
# teilbar, und im Verlauf des Browsers als eigene Seite sichtbar.
_lang_block = re.search(r'<div class="langs".*?</div>', src, re.S)
assert _lang_block, "Sprachblock nicht gefunden"
LANGS_TPL = _lang_block.group(0)

def langs_markup(cur):
    out = []
    for lg in LANGS:
        cu = ' aria-current="page"' if lg == cur else ""
        out.append('<a href="%s" hreflang="%s" data-lang="%s"%s>%s</a>'
                   % (HOME[lg], lg, lg, cu, lg.upper()))
    head = LANGS_TPL[:LANGS_TPL.index(">") + 1]
    return head + "".join(out) + "</div>"

# Die Regeln fuer die Knöpfe muessen die Links mitnehmen, sonst verliert die
# Sprachwahl ihr Aussehen.
src = src.replace(".langs button{", ".langs button,.langs a{")
src = src.replace(".langs button:hover{", ".langs button:hover,.langs a:hover{")
src = src.replace('.langs button[aria-pressed="true"]{',
                  '.langs button[aria-pressed="true"],.langs a[aria-current]{')
src = src.replace(".btn,.chip,.tellnav button,.d-reelnav button,.langs button{",
                  ".btn,.chip,.tellnav button,.d-reelnav button,.langs button,.langs a{")
src = src.replace(".langs{display:flex;gap:2px;margin-left:auto}",
                  ".langs{display:flex;gap:2px;margin-left:auto}\n"
                  ".langs a{text-decoration:none;display:inline-block}")

# ------------------------------------------------------------------ 4. Skript
# Der Erstanstrich richtet sich nach der Sprache der Datei, nicht mehr nach
# der Browsereinstellung: jede Adresse liefert immer dieselbe Sprache aus.
_fp = re.search(r'/\* first paint.*?\n\}\)\(\);', src, re.S)
assert _fp, "Erstanstrich-Block nicht gefunden"
src = src.replace(_fp.group(0),
  "/* Erstanstrich: die Sprache steht im lang-Attribut der Datei. ?lang=\n"
  "   bleibt fuer alte Links gueltig und wechselt dann im Browser. */\n"
  "(function(){\n"
  '  var q="";\n'
  '  try{q=(new URLSearchParams(window.location.search).get("lang")||"").toLowerCase();}catch(e){}\n'
  "  if(LANGS.indexOf(q)>-1){applyLang(q,false);return;}\n"
  '  applyLang(document.documentElement.lang||"de",false);\n'
  "})();", 1)

# Ein Link navigiert selbst; er darf nicht zusaetzlich im Browser umschalten.
src = src.replace(
  'for(var b=0;b<langBtns.length;b++){\n'
  '  langBtns[b].addEventListener("click",function(){\n'
  '    applyLang(this.getAttribute("data-lang"),true);\n'
  '  });\n'
  '}',
  '/* Die Sprachwahl sind jetzt Links auf echte Adressen — der Browser\n'
  '   navigiert selbst. Nur uebriggebliebene Knöpfe schalten noch um. */\n'
  'for(var b=0;b<langBtns.length;b++){\n'
  '  if(langBtns[b].tagName==="A"){continue;}\n'
  '  langBtns[b].addEventListener("click",function(){\n'
  '    applyLang(this.getAttribute("data-lang"),true);\n'
  '  });\n'
  '}')

# aria-pressed gibt es auf einem Link nicht; dort ist aria-current richtig.
src = src.replace(
  '    langBtns[j].setAttribute("aria-pressed",String(langBtns[j].getAttribute("data-lang")===l));',
  '    var on=langBtns[j].getAttribute("data-lang")===l;\n'
  '    if(langBtns[j].tagName==="A"){\n'
  '      if(on){langBtns[j].setAttribute("aria-current","page");}\n'
  '      else{langBtns[j].removeAttribute("aria-current");}\n'
  '    }else{langBtns[j].setAttribute("aria-pressed",String(on));}')

# Und die Adresse nicht mehr mit ?lang= zupflastern, wenn sie schon stimmt.
src = src.replace("if(writeUrl&&window.history&&history.replaceState){",
                  "if(writeUrl&&l!==(document.documentElement.getAttribute(\"data-page-lang\")||\"\")&&window.history&&history.replaceState){")

# ------------------------------------------------------------------ 5. Fusszeile
FOOT = {
 "de": ('<a href="/impressum/">Impressum</a>', '<a href="/datenschutz/">Datenschutz</a>'),
 "fr": ('<a href="/impressum/">Mentions légales</a>', '<a href="/datenschutz/">Protection des données</a>'),
 "it": ('<a href="/impressum/">Note legali</a>', '<a href="/datenschutz/">Protezione dei dati</a>'),
 "en": ('<a href="/impressum/">Legal notice</a>', '<a href="/datenschutz/">Privacy</a>'),
}
src = src.replace('<p class="r">tellingly.ch</p>',
                  '<p class="r foot-legal">__FOOTLINKS__</p>')
src = src.replace(".foot{", ".foot-legal a{color:inherit;text-decoration:none;border-bottom:1px solid var(--rule)}\n"
                            ".foot-legal a:hover{color:var(--ink)}\n"
                            ".foot-legal span{opacity:.45;margin:0 .55em}\n.foot{")

# ------------------------------------------------------------------ 6. Vorrendern
NODES = re.compile(r'(<(\w+)([^>]*\sdata-i18n="([^"]+)"[^>]*)>)(.*?)(</\2>)', re.S)

def render(html, lang):
    d = I18N[lang]
    def sub(m):
        key = m.group(4)
        return m.group(1) + d.get(key, m.group(5)) + m.group(6) if key in d else m.group(0)
    return NODES.sub(sub, html)

def page(lang):
    h = render(src, lang)
    d = I18N[lang]
    url = SITE + HOME[lang]

    h = h.replace('<html lang="de">', '<html lang="%s" data-page-lang="%s">' % (lang, lang), 1)
    h = re.sub(r"<title>.*?</title>", "<title>%s</title>" % d["meta.title"], h, count=1, flags=re.S)
    h = re.sub(r'(<meta name="description" content=")[^"]*(">)',
               lambda m: m.group(1) + d["meta.desc"] + m.group(2), h, count=1)

    alts = "\n".join('<link rel="alternate" hreflang="%s" href="%s%s">' % (l, SITE, HOME[l]) for l in LANGS)
    head = (
        '<link rel="canonical" href="%s">\n%s\n'
        '<link rel="alternate" hreflang="x-default" href="%s/">' % (url, alts, SITE)
    )
    og = (
        '<meta property="og:title" content="%s">\n'
        '<meta property="og:description" content="%s">\n'
        '<meta property="og:url" content="%s">\n'
        '<meta property="og:locale" content="%s">\n'
        '<meta property="og:image" content="%s/og-%s.png">\n'
        '<meta property="og:image:width" content="1200">\n'
        '<meta property="og:image:height" content="630">\n'
        '<meta property="og:image:alt" content="%s">\n'
        '<meta name="twitter:card" content="summary_large_image">\n'
        '<meta name="twitter:title" content="%s">\n'
        '<meta name="twitter:description" content="%s">\n'
        '<meta name="twitter:image" content="%s/og-%s.png">'
        % (d["meta.title"], d["meta.desc"], url,
           {"de": "de_CH", "fr": "fr_CH", "it": "it_CH", "en": "en_GB"}[lang],
           SITE, lang, d["meta.title"], d["meta.title"], d["meta.desc"], SITE, lang)
    )
    h = h.replace('<meta property="og:type" content="website">',
                  head + '\n<meta property="og:type" content="website">\n' + og, 1)

    h = h.replace(LANGS_TPL, langs_markup(lang), 1)
    imp, dat = FOOT[lang]
    h = h.replace("__FOOTLINKS__", imp + "<span>·</span>" + dat)
    return h


# ------------------------------------------------------------------ 7. Schreiben
def build():
    for lang in LANGS:
        out = DIST / ("" if lang == "de" else lang)
        out.mkdir(parents=True, exist_ok=True)
        (out / "index.html").write_text(page(lang), encoding="utf-8")

    # robots.txt und Sitemap
    (DIST / "robots.txt").write_text(
        "User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % SITE, encoding="utf-8")

    today = datetime.date.today().isoformat()
    urls = []
    for lang in LANGS:
        alts = "".join(
            '\n    <xhtml:link rel="alternate" hreflang="%s" href="%s%s"/>' % (l, SITE, HOME[l])
            for l in LANGS)
        alts += '\n    <xhtml:link rel="alternate" hreflang="x-default" href="%s/"/>' % SITE
        urls.append(
            "  <url>\n    <loc>%s%s</loc>%s\n    <lastmod>%s</lastmod>\n"
            "    <changefreq>monthly</changefreq>\n    <priority>%s</priority>\n  </url>"
            % (SITE, HOME[lang], alts, today, "1.0" if lang == "de" else "0.8"))
    for extra in ("/impressum/", "/datenschutz/"):
        urls.append("  <url>\n    <loc>%s%s</loc>\n    <lastmod>%s</lastmod>\n"
                    "    <changefreq>yearly</changefreq>\n    <priority>0.2</priority>\n  </url>"
                    % (SITE, extra, today))
    (DIST / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
        '        xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        + "\n".join(urls) + "\n</urlset>\n", encoding="utf-8")

    (DIST / "site.webmanifest").write_text(json.dumps({
        "name": "Tellingly", "short_name": "Tellingly",
        "description": I18N["de"]["meta.desc"],
        "start_url": "/", "display": "browser",
        "background_color": "#0B0C0D", "theme_color": "#0B0C0D",
        "icons": [{"src": "/icon-192.png", "sizes": "192x192", "type": "image/png"},
                  {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png"}],
    }, ensure_ascii=False, indent=2), encoding="utf-8")

    print("dist/ gebaut:")
    for f in sorted(DIST.rglob("*")):
        if f.is_file():
            print("  %-52s %7.1f kB" % (f.relative_to(DIST), f.stat().st_size / 1024))




# ==================================================================== Rechtstexte
# Entwuerfe. Sitz, UID, Handelsregister und vertretungsberechtigte Person
# kennt der Generator nicht — sie stehen als deutlich markierte Platzhalter
# drin und muessen vor dem Livegang ersetzt werden.
PH = '<mark class="ph">%s</mark>'

LEGAL_CSS = """
.legal{max-width:66ch}
.legal h1{margin:0 0 .2em;font-size:clamp(30px,4vw,44px);letter-spacing:-.03em;font-weight:400}
.legal h2{margin:2.4em 0 .5em;font-size:clamp(20px,2.2vw,26px);letter-spacing:-.02em;
  max-width:none;text-wrap:balance}
.legal h2:first-of-type{margin-top:1.2em}
.legal p,.legal li{font-size:16.5px}
.legal ul{padding-left:1.1em;margin:.6em 0}
.legal li{margin:.35em 0}
.legal dt{font:400 12.5px/1.5 var(--mono);color:var(--ink-soft);margin-top:1.1em}
.legal dd{margin:.15em 0 0}
.legal .ph{background:rgba(192,138,74,.20);color:inherit;padding:.05em .38em;
  border:1px solid rgba(192,138,74,.55);border-radius:2px}
.legal .stand{margin-top:3em;font:400 12.5px/1.6 var(--mono);color:var(--ink-soft)}
.legal .hint{border-left:2px solid var(--accent);padding:.1em 0 .1em 1em;margin:1.6em 0;color:var(--ink-soft)}
.backlink{font:400 12.5px/1.5 var(--mono);color:var(--ink-soft);text-decoration:none}
.backlink:hover{color:var(--ink)}
"""

IMPRESSUM = """
<h1>Impressum</h1>

<dl>
<dt>Firma</dt><dd>Tellingly GmbH</dd>
<dt>Sitz</dt><dd>{adresse}</dd>
<dt>Unternehmens-Identifikationsnummer</dt><dd>{uid}</dd>
<dt>Handelsregister</dt><dd>{hreg}</dd>
<dt>Vertretungsberechtigte Person</dt><dd>{person}</dd>
<dt>Kontakt</dt><dd><a href="mailto:hallo@tellingly.ch">hallo@tellingly.ch</a></dd>
</dl>

<h2>Haftung für Inhalte</h2>
<p>Die Inhalte dieser Seite wurden mit Sorgfalt erstellt. Für Richtigkeit, Vollständigkeit
und Aktualität wird keine Gewähr übernommen. Die auf dieser Seite gezeigten Rückblicke,
Dokumente und Zahlen sind Demonstrationen: sie sind plausibel konstruiert und stammen
nicht von realen Personen oder Institutionen. Sie sind keine Anlage-, Vorsorge-,
Rechts-, Bildungs- oder medizinische Beratung.</p>

<h2>Haftung für Links</h2>
<p>Diese Seite verweist an einer Stelle auf ein extern gehostetes Beispieldokument.
Für Inhalte externer Seiten ist ausschliesslich deren Betreiberin verantwortlich.
Zum Zeitpunkt der Verlinkung waren keine rechtswidrigen Inhalte erkennbar.</p>

<h2>Urheberrecht</h2>
<p>Texte, Gestaltung, Code und Bildmaterial dieser Seite sind urheberrechtlich geschützt.
Jede Verwendung ausserhalb der Schranken des Urheberrechts bedarf der schriftlichen
Zustimmung der Tellingly GmbH.</p>

<h2>Anwendbares Recht und Gerichtsstand</h2>
<p>Es gilt Schweizer Recht. Gerichtsstand ist {gerichtsstand} — soweit nicht zwingende
gesetzliche Bestimmungen etwas anderes vorschreiben.</p>
"""

DATENSCHUTZ = """
<h1>Datenschutzerklärung</h1>

<p>Diese Erklärung beschreibt, welche Personendaten beim Besuch dieser Website
bearbeitet werden. Sie richtet sich nach dem revidierten Schweizer
Datenschutzgesetz (DSG) und, soweit anwendbar, nach der Datenschutz-Grundverordnung
der EU (DSGVO).</p>

<h2>Verantwortliche Stelle</h2>
<dl>
<dt>Firma</dt><dd>Tellingly GmbH</dd>
<dt>Adresse</dt><dd>{adresse}</dd>
<dt>Kontakt in Datenschutzfragen</dt><dd><a href="mailto:hallo@tellingly.ch">hallo@tellingly.ch</a></dd>
</dl>

<h2>Was diese Website nicht tut</h2>
<p>Diese Website setzt keine Cookies. Sie verwendet keine Analyse- oder
Reichweitenmessung, keine Werbe- oder Tracking-Dienste und keine Einbindungen
sozialer Netzwerke. Sie speichert nichts im Browser. Die verwendeten Schriften
liegen auf demselben Server wie die Seite — es findet kein Aufruf bei Google
Fonts oder einem anderen Drittanbieter statt. Deshalb erscheint auf dieser
Seite auch kein Cookie-Banner: es gibt nichts einzuwilligen.</p>

<h2>Server-Protokolle</h2>
<p>Beim Abruf der Seite übermittelt Ihr Browser technisch notwendige Angaben,
die der Hosting-Dienstleister in Protokolldateien festhält:</p>
<ul>
<li>IP-Adresse des anfragenden Geräts</li>
<li>Datum und Uhrzeit des Abrufs</li>
<li>Name und URL der abgerufenen Datei</li>
<li>übertragene Datenmenge und Meldung über den Erfolg des Abrufs</li>
<li>Browsertyp, Browserversion und Betriebssystem</li>
<li>gegebenenfalls die zuvor besuchte Seite</li>
</ul>
<p>Diese Bearbeitung ist für den Betrieb und die Sicherheit der Seite erforderlich
und stützt sich auf das überwiegende Interesse an einem stabilen, missbrauchsfreien
Betrieb (Art. 31 Abs. 1 DSG; Art. 6 Abs. 1 lit. f DSGVO). Die Protokolle werden
nach {logfrist} gelöscht und nicht mit anderen Datenquellen zusammengeführt.</p>

<h2>Hosting</h2>
<p>Die Website wird bei {hoster} betrieben. Der Dienstleister bearbeitet die oben
genannten Daten als Auftragsbearbeiter, ausschliesslich weisungsgebunden und auf
Servern {serverstandort}.</p>

<h2>Kontaktaufnahme per E-Mail</h2>
<p>Wenn Sie uns schreiben, bearbeiten wir Ihre Angaben — Name, E-Mail-Adresse und
Inhalt der Nachricht — ausschliesslich zur Beantwortung Ihres Anliegens und zur
Abwicklung eines allfälligen Vertragsverhältnisses (Art. 31 Abs. 2 lit. a DSG;
Art. 6 Abs. 1 lit. b DSGVO). Wir geben diese Angaben nicht an Dritte weiter.
Korrespondenz wird gelöscht, sobald sie nicht mehr benötigt wird und keine
gesetzliche Aufbewahrungspflicht entgegensteht.</p>

<h2>Externe Verweise</h2>
<p>Diese Seite verlinkt an einer Stelle auf ein extern gehostetes Beispieldokument.
Beim Anklicken verlassen Sie diese Website; ab diesem Zeitpunkt gilt die
Datenschutzerklärung der jeweiligen Betreiberin. Auf deren Datenbearbeitung
haben wir keinen Einfluss.</p>

<h2>Datensicherheit</h2>
<p>Die Übertragung ist durchgehend mit TLS verschlüsselt; erkennbar am
<span class="mono">https://</span> in der Adresszeile. Wir treffen angemessene
technische und organisatorische Massnahmen, um Ihre Daten gegen Verlust und
unberechtigten Zugriff zu schützen.</p>

<h2>Ihre Rechte</h2>
<p>Sie haben im Rahmen des anwendbaren Rechts Anspruch auf Auskunft über die
zu Ihnen bearbeiteten Personendaten sowie auf deren Berichtigung, Löschung oder
Einschränkung der Bearbeitung; ferner auf Herausgabe oder Übertragung Ihrer
Daten. Wenden Sie sich dafür an die oben genannte Adresse. Sie können sich
zudem bei der zuständigen Aufsichtsbehörde beschweren — in der Schweiz beim
Eidgenössischen Datenschutz- und Öffentlichkeitsbeauftragten (EDÖB), in der EU
bei der Datenschutzbehörde Ihres Wohnsitzstaates.</p>

<h2>Änderungen</h2>
<p>Wir passen diese Erklärung an, wenn sich die Datenbearbeitung ändert.
Massgebend ist jeweils die hier veröffentlichte Fassung.</p>
"""


def legal_page(slug, title, body):
    """Eine Rechtsseite im Kleid der Website: gleicher Kopf, gleiche Schriften,
    gleiche Fusszeile — nur der Inhalt ist ein anderer."""
    base = page("de")
    style = "\n".join(re.findall(r"<style>(.*?)</style>", base, re.S))
    head_m = re.search(r'<header class="site">.*?</header>', base, re.S)
    head_html = head_m.group(0) if head_m else ""
    head_html = re.sub(r'href="#([a-z]+)"', r'href="/#\1"', head_html)
    head_html = head_html.replace(' aria-current="page"', "")
    foot_m = re.search(r"<footer>.*?</footer>", base, re.S)
    fonts = LOCALFONTS

    return (
        '<!doctype html>\n<html lang="de" data-page-lang="de">\n<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
        '<title>%s — Tellingly</title>\n'
        '<meta name="description" content="%s der Tellingly GmbH, Kreuzlingen.">\n'
        '<meta name="robots" content="index,follow">\n'
        '<link rel="canonical" href="%s/%s/">\n'
        '<meta name="theme-color" content="#0B0C0D">\n'
        '%s\n%s\n%s\n'
        '<style>%s%s</style>\n</head>\n<body>\n'
        '%s\n<main><section class="sec"><div class="wrap">\n'
        '<div class="legal">%s\n'
        '<p style="margin-top:2.6em"><a class="backlink" href="/">← tellingly.ch</a></p>\n'
        '</div>\n</div></section></main>\n%s\n</body>\n</html>\n'
        % (title, title, SITE, slug,
           ICONS, fonts,
           '<meta property="og:type" content="website">',
           style, LEGAL_CSS,
           head_html,
           body,
           foot_m.group(0) if foot_m else "")
    )


def legal():
    imp = IMPRESSUM.format(
        adresse=PH % "Strasse, PLZ Kreuzlingen — eintragen",
        uid=PH % "CHE-___.___.___ — eintragen",
        hreg=PH % "Handelsregister des Kantons Thurgau, eingetragen am ___ — eintragen",
        person=PH % "Name, Funktion — eintragen",
        gerichtsstand=PH % "Kreuzlingen — bestätigen",
    )
    dat = DATENSCHUTZ.format(
        adresse=PH % "Strasse, PLZ Kreuzlingen — eintragen",
        logfrist=PH % "____ Tagen — beim Hoster erfragen",
        hoster=PH % "Hostpoint AG, Rapperswil-Jona — bestätigen",
        serverstandort=PH % "in der Schweiz — bestätigen",
    )
    for slug, title, body in [("impressum", "Impressum", imp),
                              ("datenschutz", "Datenschutzerklärung", dat)]:
        out = DIST / slug
        out.mkdir(parents=True, exist_ok=True)
        (out / "index.html").write_text(legal_page(slug, title, body), encoding="utf-8")


if __name__ == "__main__":
    legal()
    build()
