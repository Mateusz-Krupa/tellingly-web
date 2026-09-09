#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Favicon, Icons und Vorschaubilder — aus der Wortmarke, nicht erfunden.

Die Marke ist typografisch (Source Serif 4). Also ist auch das Zeichen
typografisch: ein T, aus derselben Schrift geschnitten, als echter Pfad —
damit das SVG-Favicon keine Schrift nachladen muss.
"""
import pathlib, io, re, urllib.request
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools.pens.svgPathPen import SVGPathPen
from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).resolve().parent
if ROOT.name == "source":
    ROOT = ROOT.parent
DIST = ROOT / "dist"
DIST.mkdir(exist_ok=True)

INK        = (0x16, 0x19, 0x1A)
PAPER      = (0xE7, 0xE7, 0xE1)
PAPERBRIGHT= (0xF7, 0xF7, 0xF4)
ACCENT     = (0x2E, 0x5B, 0x49)
FIELD      = (0x2A, 0x2E, 0x30)
SOFT       = (0x9A, 0xA2, 0x9C)

# Zum Rendern brauchen wir die vollstaendigen Schriften, nicht die Subsets:
# die latin-Datei allein hat kein ł und kein ą, das polnische Vorschaubild
# bekaeme sonst Ersatzkaesten. Die v1-API liefert die ungeteilte TTF.
FULL = {
    "serif-sb": "https://fonts.googleapis.com/css?family=Source+Serif+4:600&subset=latin,latin-ext",
    "serif-rg": "https://fonts.googleapis.com/css?family=Source+Serif+4:400&subset=latin,latin-ext",
    "mono":     "https://fonts.googleapis.com/css?family=IBM+Plex+Mono:400&subset=latin,latin-ext",
}
CACHE = pathlib.Path("/tmp/tg-fonts"); CACHE.mkdir(exist_ok=True)

def fetch(name):
    ttf = CACHE / (name + ".ttf")
    if not ttf.exists():
        req = urllib.request.Request(FULL[name], headers={"User-Agent": "Mozilla/4.0"})
        css = urllib.request.urlopen(req).read().decode()
        url = re.search(r"url\((https://[^)]+\.ttf)\)", css).group(1)
        urllib.request.urlretrieve(url, ttf)
    return ttf

SERIF_VF = DIST / "fonts" / "source-serif-4-300-normal-latin.woff2"

def static(woff2, **axes):
    """Eine feste Schnittstelle aus der variablen Schrift schneiden (nur fuers SVG)."""
    f = TTFont(woff2)
    f.flavor = None
    if axes and "fvar" in f:
        f = instancer.instantiateVariableFont(f, axes, inplace=False)
    buf = io.BytesIO()
    f.save(buf)
    return buf.getvalue()

SERIF_SB = static(SERIF_VF, wght=600, opsz=60)     # Umriss fuer das Favicon

def pil(name, size):
    return ImageFont.truetype(str(fetch(name)), size)


# ---------------------------------------------------------------- 1. SVG-Favicon
def svg_favicon():
    f = TTFont(io.BytesIO(SERIF_SB))
    upm = f["head"].unitsPerEm
    gs = f.getGlyphSet()
    gname = f.getBestCmap()[ord("T")]
    pen = SVGPathPen(gs)
    gs[gname].draw(pen)
    path = pen.getCommands()
    adv = gs[gname].width

    # Das T sitzt mittig auf einem quadratischen Feld, optisch etwas hoeher
    # als die geometrische Mitte — sonst wirkt es abgesackt.
    cap = f["OS/2"].sCapHeight if hasattr(f["OS/2"], "sCapHeight") else int(upm * 0.66)
    box = upm * 1.30
    dx = (box - adv) / 2
    dy = (box + cap) / 2 - upm * 0.035

    # Das SVG dreht sich in dunklen Browserleisten um: dunkle Kachel auf
    # hellem Chrome, helle Kachel auf dunklem. Ein Favicon, das in beiden
    # Faellen verschwindet, ist keines.
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d">'
        '<style>'
        '.tile{fill:#16191A}.mark{fill:#E7E7E1}'
        '@media (prefers-color-scheme:dark){'
        '.tile{fill:#E7E7E1}.mark{fill:#16191A}}'
        '</style>'
        '<rect class="tile" width="%d" height="%d" rx="%d"/>'
        '<g class="mark" transform="translate(%.1f %.1f) scale(1 -1)">'
        '<path d="%s"/></g></svg>'
        % (box, box, box, box, int(box * 0.14), dx, dy, path)
    )
    (DIST / "favicon.svg").write_text(svg, encoding="utf-8")
    return svg


# ---------------------------------------------------------------- 2. Raster-Icons
def raster_icon(px, radius_ratio=0.14, bleed=False):
    """bleed=True: randlos, fuer apple-touch-icon (iOS rundet selbst)."""
    S = px * 8
    im = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    r = 0 if bleed else int(S * radius_ratio)
    d.rounded_rectangle([0, 0, S - 1, S - 1], radius=r, fill=INK + (255,))
    fnt = pil("serif-sb", int(S * 0.70))
    box = d.textbbox((0, 0), "T", font=fnt)
    d.text(((S - (box[2] - box[0])) / 2 - box[0],
            (S - (box[3] - box[1])) / 2 - box[1] - S * 0.015),
           "T", font=fnt, fill=PAPER + (255,))
    return im.resize((px, px), Image.LANCZOS)


def icons():
    svg_favicon()
    # 16 und 32 gehen in die .ico — die frisst noch jeder Feedreader und Windows
    ico = [raster_icon(s).convert("RGB") for s in (16, 32, 48)]
    ico[0].save(DIST / "favicon.ico", format="ICO",
                sizes=[(16, 16), (32, 32), (48, 48)])
    raster_icon(180, bleed=True).convert("RGB").save(DIST / "apple-touch-icon.png")
    raster_icon(192).save(DIST / "icon-192.png")
    raster_icon(512).save(DIST / "icon-512.png")


# ---------------------------------------------------------------- 3. Vorschaubild
CLAIM = {
    "de": "Daten, erzählt.",
    "fr": "Les données, racontées.",
    "it": "I dati, raccontati.",
    "en": "Data, told.",
}
SUB = {
    "de": "Institutionen verschicken Daten. Menschen lesen sie nicht.",
    "fr": "Les institutions envoient des données. Personne ne les lit.",
    "it": "Le istituzioni spediscono dati. Nessuno li legge.",
    "en": "Institutions send data. People do not read it.",
}
# Dieselben Zeilen wie im Hero-Feld: ein Vorsorgeausweis, wie er ankommt.
FIELDLINES = [
    "Vorsorgeausweis / Certificat de prevoyance    gueltig ab 01.01.2027",
    "Gemeldeter Jahreslohn                                   118 400.00",
    "Koordinationsabzug                                       -26 460.00",
    "Versicherter Lohn                                         91 940.00",
    "Altersguthaben 31.12.2026                                301 661.50",
    "Altersgutschrift 2027   15.0 %                            13 791.00",
    "Zinssatz obligatorisch 1.25 %   ueberobligatorisch 1.00 %",
    "Voraussichtliche Altersrente ab 65                        18 099.70",
    "Voraussichtliche Altersrente ab 62                        14 902.30",
    "Invalidenrente                                            45 970.00",
    "Ehegattenrente                                            27 582.00",
    "Waisenrente                                                9 194.00",
    "Sparbeitrag Arbeitnehmer                                     574.62",
    "Moeglicher Einkauf per 01.01.2027                         64 209.00",
    "Freizuegigkeitsleistung                                  301 661.50",
    "Deckungsgrad der Kasse                                       108.4 %",
]


def og(lang):
    W, H = 1200, 630
    im = Image.new("RGB", (W, H), INK)
    d = ImageDraw.Draw(im)

    # Das Dokumentfeld im Hintergrund — dasselbe Bild wie auf der Seite:
    # das Papier, das ankommt und nicht gelesen wird.
    fm = pil("mono", 13)
    y, i = 26, 0
    while y < H:
        d.text((40, y), FIELDLINES[i % len(FIELDLINES)], font=fm, fill=FIELD)
        d.text((640, y), FIELDLINES[(i + 7) % len(FIELDLINES)], font=fm, fill=FIELD)
        y += 25
        i += 1

    # Unter der Fusszeile bleibt das Feld weg — sonst laeuft die Wortmarke
    # in die Zahlen hinein und wird unlesbar.
    d.rectangle([0, H - 132, W, H], fill=INK)
    d.rectangle([0, H - 132, W, H - 131], fill=(0x2F, 0x33, 0x35))

    # Die Karte darueber: der Satz, der daraus wird.
    m, cy, ch = 74, 150, 330
    d.rectangle([m, cy, W - m, cy + ch], fill=PAPERBRIGHT)

    fc = pil("serif-sb", 82)
    claim = CLAIM[lang]
    while d.textlength(claim, font=fc) > (W - 2 * m) - 96 and fc.size > 48:
        fc = pil("serif-sb", fc.size - 4)
    d.text((m + 48, cy + 92), claim, font=fc, fill=INK)

    fs = pil("serif-rg", 27)
    d.text((m + 48, cy + 214), SUB[lang], font=fs, fill=(0x4E, 0x54, 0x4F))

    # Fusszeile: Wortmarke links, Domain rechts
    fw = pil("serif-sb", 34)
    d.text((m, H - 88), "Tellingly", font=fw, fill=PAPER)
    fd = pil("mono", 20)
    dom = "tellingly.ch"
    d.text((W - m - d.textlength(dom, font=fd), H - 80), dom, font=fd, fill=SOFT)

    # Ein Akzentstrich, so lang wie die Wortmarke — das einzige Farbelement
    wlen = d.textlength("Tellingly", font=fw)
    d.rectangle([m, H - 40, m + wlen, H - 37], fill=ACCENT)

    p = DIST / ("og-%s.png" % lang)
    im.save(p, optimize=True)
    return p


if __name__ == "__main__":
    icons()
    for lg in CLAIM:
        p = og(lg)
        print("%-3s %-22s %5.1f kB" % (lg, p.name, p.stat().st_size / 1024))
    for n in ["favicon.svg", "favicon.ico", "apple-touch-icon.png",
              "icon-192.png", "icon-512.png"]:
        f = DIST / n
        print("%-22s %5.1f kB" % (n, f.stat().st_size / 1024))
