# Tellingly — Website

`index.html` an der Wurzel ist die gewählte Fassung — die laute Fassung (`versions/bold/`). Jede Fassung ist eine einzige, in sich geschlossene Datei ohne Build-Schritt, ohne Framework, ohne Backend. Doppelklick genügt zum Ansehen; zum Hosten reicht jeder Static-Host (Netlify, Cloudflare Pages, GitHub Pages, ein normaler Webspace). Externe Abhängigkeiten: die beiden Schriften von Google Fonts, in der 3D-Fassung zusätzlich Three.js von cdnjs.

Vier Fassungen, je ein Ordner:

| Ordner | Fassung | Einstieg |
|---|---|---|
| `versions/bold/` | **dunkel, laut** — die gewählte Fassung, auch als `index.html` | Dasselbe Hero, deutlich mehr Bewegung |
| `versions/quiet/` | ruhig, hell | Das gesetzte Hero mit dem laufenden Dokumentfeld |
| `versions/3d/` | Der Abdruck — dunkel, WebGL | Eine Fläche, fünf Zustände: Auszug, Licht, Satz, Formate, Zustellung |
| `versions/story/` | dunkel, Prolog | Fünftausend Jahre Kulturgeschichte als gescrollter Vorspann |

`versions/bold/index.html` und `index.html` sind identisch.

`direction-3d.html` ist kein Website-Entwurf, sondern die Regie dazu: das vollständige 3D-Konzept «Der Abdruck» — Narrativ, Art Direction, Komposition, Typografie, Farbe als Substanz, Material, Licht, Tiefe, Kamerasprache, emotionaler Bogen, Seitenarchitektur, Hero-Spezifikation, Motion-System, Zugänglichkeit, Produktion. Der Hero dieses Dokuments läuft in Echtzeit (Three.js): das Streiflicht folgt dem Zeiger, und die Schrift auf dem Körper erscheint und verschwindet mit dem Winkel.

Alle vier teilen Inhalt, Sprachen und Bühne — ab der Sektion «Argument» ist die Seite in jeder Fassung dieselbe. Sie unterscheiden sich im Einstieg, im Ton und in der Bewegung.

`build.py` erzeugt `versions/quiet/index.html`. `bold.py` und `story.py` lesen diese Datei und schreiben daraus `versions/bold/` bzw. `versions/story/` — beide sind reine Zusatzschichten aus einem zweiten Stylesheet und einem zweiten Script. `bold.py` schreibt zusätzlich die Wurzel-`index.html`. `abdruck.py` liest ebenfalls die ruhige Fassung, ersetzt darin das Hero durch die WebGL-Sequenz und schreibt nach `versions/3d/`. Reihenfolge beim Neubauen: `build.py`, dann die drei anderen.

Nötig ist das nicht — jede `index.html` lässt sich direkt bearbeiten. Die Demo-Inhalte stehen im Script am Ende der Datei in zwei Objekten: `DEMO` (die Rückblicke) und `WHY` (die Argumente), beide nach Sprache und Bereich sortiert. Der Text der fünf Akte der 3D-Fassung steht in `abdruck_copy.py`.

---

## Getroffene Entscheidungen

**Eine Seite, keine Unterseiten.** Das Argument der Firma ist eine Abfolge: Problem → Ursprung → Formate → Bereiche → Ausprobieren → Abgrenzung. Diese Kette zerfällt, wenn man sie auf Unterseiten verteilt. Ausserdem gibt es vor dem Launch nichts, was Tiefe rechtfertigen würde.

**Deutsch als Standard, vier Sprachen.** Die Käufer sind deutschsprachige Schweizer Institutionen. Deutsch, Französisch, Italienisch, Englisch — die drei Landessprachen plus Englisch. Im ausgelieferten Ordner hat jede Sprache eine eigene Adresse (`/`, `/fr/`, `/it/`, `/en/`); `?lang=xx` bleibt als alter Link gültig, `hreflang` ist gesetzt. Ohne JavaScript bleibt die vollständige deutsche Seite bestehen — der deutsche Text steht im HTML, nicht im Script.

**Kontakt per Mailto.** Kein Backend, also kein Formular ohne Fremddienst. Ein Mailto ist für institutionelle Käufer ohnehin das erwartete Verhalten.

**Produktnamen bleiben unübersetzt** (Portfolio, Pension, School, Health, Team / Reel, Brief, Edition). Vertragsname ist die Schreibweise mit Leerzeichen («Pension Brief»); die Punkt-Schreibweise `pension.brief` erscheint nur einmal, über der Bühne, in Mono und Kleinschrift — nie als Link.

---

## Gestaltung

**Das Hero ist die eine mutige Stelle.** Der Hintergrund ist ein institutionelles Dokument: dicht gesetzte Zahlen, Falzlinien an den Dritteln, wie ein Brief im Couvert. Darüber liegt ein Fenster — die Sichtöffnung eines Schweizer Fenstercouverts —, und was durchscheint, ist nicht die Adresse, sondern der Satz. Das ist gleichzeitig Problem, Referenz und der Moment des Öffnens.

**Fünf Dokumente, fünf Sätze.** Das Hero deckt alle fünf Bereiche ab: Portfolioauszug (Bank), Vorsorgeausweis (Pensionskasse), Zeugnis (Schule), Laborbefund (Gesundheit), Mitarbeiterbeurteilung (HR). Hintergrunddokument und Satz wechseln gemeinsam, alle 5.4 Sekunden; die Zeile unter dem Couvert benennt das jeweilige Dokument und ist anklickbar. Ein Klick hält den Wechsel an, Mouseover pausiert ihn. Bei `prefers-reduced-motion` gibt es keinen automatischen Wechsel, die Auswahl bleibt bedienbar. Ohne JavaScript steht der erste Fall.

Die fünf Sätze liegen übereinander in derselben Zelle, das Fenster ist deshalb immer so hoch wie der längste — beim Wechsel springt nichts. Alles andere auf der Seite ist ruhig.

**Bewusst vermieden**, weil in der Aufgabenstellung als generisch markiert: Creme `#F4F1EA` mit Terrakotta, gesperrte Versal-Labels, 01/02/03-Marker, Mittelpunkt-Ketten, `→` an Links, Fade-up beim Scrollen (es gibt gar keine Scroll-Animation), farbig hervorgehobene Einzelwörter in Überschriften. Auch der Broadsheet-Look mit Haarlinien wurde umgangen: die Referenz ist das Buchhaltungsjournal und das Amtsformular, nicht die Zeitung.

**Palette.** Papier `#E7E7E1` (kühles Grau-Oat, nicht Creme), Tinte `#16191A`, ein einziger Akzent in Archivgrün `#2E5B49`. Schriften: Source Serif 4 (kontrastarm, Dokument- statt Zeitschriftenserife) und IBM Plex Mono für Zahlen und Marginalien.

**Formate-Sektion mit echten Vorschauen.** Drei Formate, drei Seitenverhältnisse, dreimal derselbe Inhalt:

- **Reel** — Hochkant, abgerundet wie ein Telefondisplay, mit Story-Balken oben und der grossen Zahl unten. Das Spotify-Wrapped-Pendant.
- **Brief** — Seitenformat 4:5, ein scrollender Bericht im Browser: Titel, Absatz, Zwischentitel. Darunter der Link auf den funktionierenden Portfolio Brief.
- **Edition** — Doppelseite 16:10, gedruckt.

Alle drei zeigen denselben Rückblick: «Ihr Jahr in dreissig Sekunden», −3.12 %, «Was Ihr Portfolio bewegte». Genau das ist das Argument der Sektion — die Form macht es, nicht die Beschriftung. Die Vorschauen sind in der Typografie der Website gesetzt, nicht als Screenshots: so bleiben sie in allen vier Sprachen lesbar und altern nicht mit dem Produkt.

**Video ist entfallen.** Genannt wurden Reel, Brief und Edition — Video kam nicht mehr vor. Es ist in einem Schritt wieder einzusetzen (Formatliste, Kombinator-Chips, drei Textbausteine pro Sprache), falls es doch bleiben soll.

**Kein Diagramm auf der Seite.** Eine Grafik würde genau das Gegenteil der These behaupten.

**Qualität.** WCAG AA geprüft (schlechtestes Textverhältnis 5.7:1; der Live-Link liegt bei 7.2:1), sichtbarer Tastaturfokus, `prefers-reduced-motion` respektiert, semantisches HTML inkl. echter Tabelle, kein horizontales Scrollen bis 390 px, Druck-Stylesheet vorhanden.

---

## Ausprobieren — die Sektion, in der man es erlebt

Die frühere Sektion «Wir beginnen bei der Vorsorge» ist entfallen. Der Vorsorge-Fall lebt jetzt in der Bühne (Bereich «Pension») und im Argument darunter; der Hinweis auf die ersten Pensionskassen-Partner steht weiterhin im Kontakt-Abschnitt.

Nach «Bereiche» steht jetzt eine Bühne. Man wählt einen Bereich und ein Format, und darunter läuft das echte Erzeugnis — nicht ein Bild davon.

**Fünfzehn Kombinationen, vier Sprachen.** Jeder der fünf Bereiche hat einen eigenen Rückblick: Titel, vier Kennzahlen, zwei erzählende Passagen und einen Schlusssatz, der auf ein Gespräch zeigt. Dieselben Bausteine werden von drei Renderern verschieden zugestellt:

- **Reel** — ein Telefon mit Story-Balken. Weiter mit den Schaltflächen oder mit einem Tipp auf die Karte, sechs Karten pro Bereich, Tastatur inklusive.
- **Brief** — eine scrollende Seite. Man scrollt wirklich; die Kante unten blendet aus, damit man es sieht.
- **Edition** — eine Doppelseite mit Folio, links die Erzählung, rechts die Kennzahlen und der Schluss. Auf dem Telefon stapeln sich die beiden Seiten.

Alle 75 Kombinationen (5 Bereiche × 3 Formate × 5 Sprachen) wurden automatisiert durchgeklickt und gerendert.

**Ohne Marke — und das ist das Argument.** Die Bühne hat eine eigene, neutrale Oberfläche: weisses Papier, schwarze Tinte, kein Grün, keine Serife aus dem Tellingly-Auftritt. Wo das Logo des Kunden stünde, steht ein gestricheltes Rechteck. Die Zeile darüber sagt es ausdrücklich: Farbe, Schrift und Logo kommen vom Kunden. Was man sieht, ist die Mechanik, nicht die Verpackung.

**Ohne JavaScript** steht der Pension Brief auf Deutsch fertig im HTML, samt Argument — die Sektion ist nie eine leere Box.

## Wofür — das Argument je Käufer

Unter der Bühne steht, wozu der jeweilige Bereich dient, mit drei konkreten Ergebnissen. Es wechselt mit dem gewählten Bereich:

- **Portfolio** — der Auszug ist der einzige garantierte Kontaktpunkt mit jedem Kunden. Gelesen statt abgelegt, Termine aus dem Versand, persönlicher Bezug statt Standardreporting.
- **Pension** — gesetzlich vorgeschrieben und trotzdem ungelesen. Weniger Rückfragen, bewusstere Entscheide zu Einkauf und Rentenalter, Vertrauen in eine Institution, die man nie sieht.
- **School** — Eltern lesen Noten und übersehen den Verlauf. Vorbereitete Eltern, weniger Diskussion über Einzelnoten, sichtbarer Fortschritt.
- **Health** — ein unverstandener Befund erzeugt Angst oder Gleichgültigkeit. Höhere Termintreue, weniger beunruhigte Anrufe, Prävention, die ankommt.
- **Team** — geschrieben, unterschrieben, vergessen. Beurteilungen, an die man sich erinnert, bessere Entwicklungsgespräche, ein Signal an Mitarbeitende.

---

## Bewegung — begründet, nicht dekorativ

Die Website selbst animiert nichts: kein Fade-up beim Scrollen, keine Scroll-Animation, nirgends. Innerhalb der Bühne gilt das Gegenteil, weil dort nicht die Website zu sehen ist, sondern das Produkt. Die Trennlinie ist die ganze Regel: **das Blatt steht still, das Erzeugnis bewegt sich — und nur dort, wo die Bewegung eine Kennzahl erklärt.**

Jede Art von Zahl bekommt deshalb ihre eigene Form:

| Art der Kennzahl | Element | Warum diese Bewegung |
|---|---|---|
| Betrag, angespart | Zähler, der hochläuft | Ein Guthaben ist über Zeit entstanden; das Hochzählen führt die Entstehung noch einmal vor. Bei der Vorsorge kommt ein zweigeteilter Balken dazu: eigene Beiträge und Zins. |
| Veränderung über ein Jahr | Linie, die sich von links nach rechts zeichnet | Eine Rendite hat einen Verlauf. Die Zahl allein verschweigt, dass es im Februar wackelte. Bewusst ohne Achsen und Beschriftung — eine Geste, kein Diagramm. |
| Differenz zwischen zwei Werten | zwei Balken, der zweite verzögert | Die Botschaft ist die Lücke. Beide von null wachsen zu lassen macht das Zukurzkommen zum letzten, was ankommt. |
| Anteil an einer Menge | Punktraster, das sich füllt | «9 von 15» ist abzählbar. Ein Raster lässt das Auge prüfen, statt eine Prozentzahl zu glauben. Kein Kuchendiagramm. |
| Laborwert mit Referenz | Marke, die in ihre Skala fährt | Ein Wert ohne Referenzbereich bedeutet nichts. Der Weg der Marke in den grauen Bereich hinein — oder daran vorbei — ist die eigentliche Aussage. |
| Zielerreichung über einer Marke | Balken, der die 100-Prozent-Marke überfährt | «101.4 %» ist eine Zahl; der Balken, der über den Strich hinausläuft, ist ein Ergebnis. |
| Abzählbare Einheiten | Striche, die einzeln erscheinen | Vier Absenzen, zwölf Weiterbildungstage, drei Monate: Einheiten sollen als Einheiten erscheinen. |
| Vergleich mit dem Vorjahr | Zähler, der beim Vorjahreswert beginnt | Der Notenschnitt läuft von 4.77 auf 4.96, nicht von null. Die Bewegung ist genau die Verbesserung. |
| Ein Name statt einer Zahl | Wort, das sich aufblendet | Nichts zu quantifizieren; die Spannung liegt im Nennen. Also wird das Wort aufgezogen wie ein Vorhang. |

**Reihenfolge im Reel.** Jede Karte baut sich in Leserichtung auf: erst die Bezeichnung, dann die Zahl, dann das Element, dann der Satz — Abstände von 70 Millisekunden. Der Blick wird geführt, nicht überrascht.

**Der Brief animiert beim Ankommen**, nicht beim Laden: jede Kennzahl startet, wenn sie in den Lesebereich scrollt, und genau einmal. Der Text selbst bewegt sich nie — nur die Zahl und ihr Element. Das ist der Unterschied zwischen «erklärt» und «zappelt».

**Die Edition bewegt sich gar nicht.** Sie zeigt dieselben Elemente im Endzustand — gedrucktes Papier animiert nicht. Dass die Vorschau still steht, ist die Aussage, kein Fehler.

**Bei `prefers-reduced-motion`** rendert alles sofort im Endzustand, inklusive der Zähler. Ohne JavaScript ebenso.

---

## Variante B — die laute Fassung (`index-bold.html`)

Referenzen: subscrr (dunkler Grund, hoher Kontrast, Produkt als Held), heron (Karten, Umschalter, Politur), oxigen (überdimensionierte Display-Typo, ganzflächige Abschnitte, Funktion vor Zierrat). Aus allen dreien ist das genommen, was zur Sache passt, nicht das Vokabular.

**Die Grundidee.** Der Grund wird schwarz (`#0B0C0D`), das Dokument bleibt weiss. Damit dreht sich das Bild um: nicht mehr ein Blatt mit einem Fenster darin, sondern ein Lichtkörper in einem dunklen Raum. Das Couvert wird zur Bühne, jedes Erzeugnis leuchtet. Feines Korn liegt über allem, damit Schwarz nicht wie eine leere Fläche wirkt.

**Was sich bewegt, und warum:**

1. **Leseanzeige** — ein zwei Pixel dünner Verlauf von Grün nach Messing am oberen Rand. Bei einer langen Einzelseite ist der Fortschritt eine echte Information.
2. **Überschriften steigen aus einer Maske** — Wort für Wort, 42 ms versetzt, von unten. Kein Fade-up: die Wörter werden gesetzt, nicht eingeblendet. Das ist die Bewegung eines Satzes, der entsteht.
3. **Der Ausdruck läuft heraus** — das Dokument im Hero wird von oben nach unten aufgedeckt, wie Papier aus einem Drucker. Bei jedem Wechsel neu.
4. **Das Couvert reagiert auf den Zeiger** — der Zahlenteppich verschiebt sich parallaktisch, das Fenster kippt leicht in die Tiefe, ein weiches Licht wandert über die Öffnung. Das ist der Moment des Anhebens.
5. **Der Hero-Satz setzt sich wortweise** — dieselbe Maske wie bei den Überschriften, synchron zum Dokumentwechsel.
6. **Magnetische Bedienelemente** — Schaltflächen und Chips ziehen leicht zum Zeiger und federn zurück; die Haupttaste füllt sich von unten.
7. **Die fünf Dokumente laufen durch** — ein Laufband über der Bereichstabelle, auf Hover angehalten. Es sagt in einer Zeile, was die Tabelle in fünf Zeilen sagt.
8. **Die Auswahl bekommt eine Pille** — ein grüner Block gleitet zwischen den Chips, statt dass jeder Chip seine Farbe wechselt. Die Auswahl wird zu einer Bewegung.
9. **Jeder Bereich bringt sein eigenes Licht** — der Schein über der Bühne wechselt den Farbton je nach Bereich (Portfolio grün, Vorsorge blau, Schule bernstein, Gesundheit rosé, Team violett). Fünf Bereiche, fünf Stimmungen, eine Mechanik.
10. **Das Format morpht** — beim Wechsel skaliert und entschärft sich das alte Erzeugnis, das neue federt aus der Unschärfe herein.
11. **Das Reel spielt sich selbst** — 4,2 Sekunden pro Karte, der Story-Balken füllt sich sichtbar mit. Hover pausiert, ein Klick übergibt die Kontrolle endgültig an den Besucher, Wischen auf dem Telefon funktioniert. Genau so verhält sich das Produkt.
12. **Tabellenzeilen treten vor** — beim Überfahren rückt die Zeile nach rechts und ein kurzer Akzentstrich erscheint links.
13. **Die Format-Vorschauen erwachen unter dem Zeiger** — das Reel hebt an, die Edition öffnet ihre zweite Seite perspektivisch, der Brief schiebt seinen Text hoch.

**Was gleich bleibt:** Inhalt, vier Sprachen, alle fünfzehn Kombinationen, die Kennzahl-Elemente und ihre Logik, das Argument je Käufer, die Semantik.

**Was abgeschaltet wird.** Bei `prefers-reduced-motion` verschwinden Leseanzeige und Laufband, alle Masken stehen offen, das Reel spielt nicht von selbst, das Couvert kippt nicht. Ohne JavaScript ist die Fassung eine ruhige, vollständige dunkle Seite — die Bewegungsschicht ist additiv, nichts hängt an ihr.

Geprüft: alle 75 Kombinationen, kein horizontales Scrollen auf 390 px, keine Konsolenfehler, Überschriften ohne JavaScript vollständig lesbar.

---

## Variante C — der Prolog (`index-story.html`)

Die Firma behauptet, das Erzählen sei älter als die Buchhaltung und beide gehörten zusammen. Diese Fassung behauptet es nicht, sie führt es vor: Bevor die Seite beginnt, scrollt man durch fünftausend Jahre. Fünf Akte auf einer klebenden Bühne, der Boden wandert dabei von Höhlenschwarz über Ton und Ocker ins kalte Grau von heute und zuletzt ins Papier der Website — der Übergang in die eigentliche Seite ist deshalb nahtlos, man merkt nicht, wo der Prolog endet.

**Akt 1 — das Feuer.** Vier Silhouetten sitzen um eine Flamme, die wirklich flackert; Funken steigen auf und driften seitlich weg. An der Wand darüber zeichnen sich beim Scrollen eine Handschablone und daneben eine Reihe Kerbstriche — jemand war hier, und jemand hat gezählt. Das ist die Gründungsthese in einem Bild, bevor ein einziger Satz sie ausspricht.
*«Am Anfang sass jemand am Feuer und erzählte, was geschehen war.»*

**Akt 2 — Uruk, 3400 v. Chr.** Eine Tontafel kippt aus der Tiefe heran, und dann werden dreiundsechzig Keilschriftzeichen einzeln hineingedrückt, im Takt des Scrollens. Sind sie gesetzt, treten sie zurück und darunter wird lesbar, was tatsächlich dort stand: `8 gur she — 3 udu — 2 gud`. Gerste, Schafe, Rinder.
*«Die erste Schrift war keine Geschichte. Sie war eine Abrechnung über Gerste und Vieh.»*

**Akt 3 — die Trennung.** Das Register driftet nach links und wird immer dichter, die Erzählung driftet nach rechts und verlischt. Auf halbem Weg erscheint oben die Zwischenmarke: Venedig, 1494 — die doppelte Buchführung bekommt ihre Grammatik, die Erzählung bekommt keine.
*«Das Buch wurde immer genauer. Die Erzählung ging verloren.»*

**Akt 4 — heute.** Der Vorsorgeausweis, unscharf, kalt, und darüber legt sich ein Siegelring, der nie gebrochen wurde.
*«Was bei Ihnen ankommt, ist genau, vollständig — und ungeöffnet.»*

**Akt 5 — die Übergabe.** Aus einer sechs Pixel hohen Linie öffnet sich eine helle Fläche: dieselbe Sichtöffnung, mit der die Website arbeitet. Der Boden ist inzwischen Papier, die Schrift kippt von Hell auf Dunkel, und der Prolog geht in das Hero über.
*«Wir setzen die beiden wieder zusammen.»*

**Ein Lineal rechts** hält die Zeit fest — 40 000 v. Chr., 3400 v. Chr., 1494, heute — mit einem Punkt, der mit dem Scrollen wandert. Es ist das einzige Element, das die ganze Zeit sichtbar bleibt.

**Bedienbar bleibt alles.** Die Kopfzeile liegt über dem Prolog und wechselt nur die Farben; Sprachwechsel funktioniert mitten in der Erzählung, alle vier Fassungen sind vollständig übersetzt, inklusive der Jahreszahlen (`40 000 v. Chr.` / `40,000 BC`). Ein Sprunglink direkt am Anfang überspringt den Prolog für Tastaturnutzer.

**Bei `prefers-reduced-motion`** verschwindet die Bühne ganz: der Prolog wird zu fünf ruhig untereinander gesetzten Zeilen, die Seite ist rund fünf Bildschirmhöhen kürzer und beginnt fast sofort. Ohne JavaScript steht der erste Akt als Text da und die Seite läuft normal weiter.

**Kosten, ehrlich gesagt.** Der Prolog verlangt fünfeinhalb Bildschirmhöhen Geduld, bevor das erste Verkaufsargument fällt. Für eine Warmakquise bei einer Pensionskasse ist das viel. Er lohnt sich, wenn die Seite aus einem Gespräch heraus geöffnet wird oder auf einer Bühne läuft — nicht unbedingt, wenn ein Beschaffungsverantwortlicher fünf Anbieter nebeneinander prüft. Deshalb ist es eine eigene Datei und nicht die Startseite.

---

## Variante D — die 3D-Fassung (`versions/3d/`, zugleich `index.html`)

Diese Fassung erzählt keine Kulturgeschichte. Sie zeigt das Produkt selbst — als Körper, im Licht.

Die These der Firma lautet: dieselben Zahlen, anders beleuchtet, ergeben eine Aussage. Genau das ist hier kein Bild, sondern die Mechanik. Der Text steht als Höhenrelief in einer Fläche; ob man ihn lesen kann, hängt allein vom Winkel der einzigen Lichtquelle ab. Fünf Akte, ein Körper, ein Licht.

**Akt I — Der Auszug.** Der Vorsorgeausweis, zweihundert Zeilen, in eine kalte, tiefe Fläche geprägt. Das Licht steht bei fünf Grad, fast parallel zur Fläche: man sieht, dass da etwas Geordnetes steht, lesen kann man es nicht. Blaugrau, hohe Selbstverschattung, kaum Streulicht.
*«Alles steht darin. Gelesen wird es nicht.»*

**Akt II — Der Blickwinkel.** Dasselbe Relief, kein Buchstabe wurde geändert. Das Licht steigt auf sechsundzwanzig Grad und wird warm, die Schlagschatten werden kurz, die Kamera geht heran — und die Zeilen sind lesbar. Das ist das ganze Versprechen in einer einzigen Bewegung, ohne ein Wort.
*«Dieselben Zahlen. Ein anderes Licht.»*

**Akt III — Die Übersetzung.** Eine weiche Kante läuft über die Fläche; wo sie vorbei ist, steht nicht mehr die Tabelle, sondern der Satz: *Sie haben dieses Jahr 36 657 Franken dazugewonnen.* Klein darunter bleibt die Rechnung stehen, aus der er kommt. Das Blatt hebt sich dabei leicht aus der Ebene.
*«Aus zweihundert Zeilen wird ein Satz.»*

**Akt IV — Drei Oberflächen.** Die Fläche teilt sich in drei Felder — Reel, Brief, Edition — und das Licht schwenkt zur Seite. Jedes Feld fällt anders aus, weil es anders im Licht liegt.
*«Ein Text. Als Reel, als Brief, als Edition.»*

**Akt V — Zugestellt.** Das Licht wird breit und warm, die Fläche wird Papier, die Strahlen bekommen einen sichtbaren Kern, das Relief glimmt leicht nach. Die fertige Seite liegt da, und die Website beginnt.
*«Und dann wird er gelesen.»*

### Was technisch darunter liegt

Kein Modell, keine Textur von aussen: die vier Höhenkarten werden beim Laden im Canvas gezeichnet — der Vorsorgeausweis, der Satz, die drei Felder, die fertige Seite — und als Graustufen an die Grafikkarte gegeben.

- **Reliefmapping mit Selbstverschattung** (Parallax Occlusion). Der Blickstrahl läuft in vierundzwanzig Schritten in die Fläche hinein, bis er auf das Höhenfeld trifft; ein Sekantenschritt nimmt der Silhouette danach die Treppe. Ein zweiter Marsch, zehn Schritte entlang der Lichtrichtung, entscheidet, ob eine Stelle im Schatten einer höheren liegt. Deshalb wandern die Schatten mit dem Licht, statt aufgemalt zu sein.
- **Material statt Farbe:** Normale aus dem Höhengradienten, Umgebungsverdeckung aus der Nachbarschaft, Glanzlicht und ein Kantenschimmer. Die Fläche bekommt ein feines Mikrorelief, damit sie nie perfekt glatt wirkt.
- **Der Übergang ist eine Kante, kein Mittelwert.** Zwei Höhenfelder ineinander zu blenden ergibt Matsch; hier läuft eine schmale, leicht verrauschte Front über die Fläche, links davon steht das eine Feld, rechts das andere.
- **Nachbearbeitung** in einem zweiten Durchgang: Lichtstrahlen aus achtzehn Abtastungen in Richtung der Lichtquelle, ein Kern für die Quelle selbst, Bloom, ACES-Tonwertkurve, Farbsaum, Vignette, Filmkorn. Dazu fünfhundertsechzig Staubpartikel, additiv, die nur im Strahl sichtbar werden.
- **Zwei Stufen Notbremse:** bleibt die Bildrate zwei Sekunden unter dreissig, fallen Pixeldichte und halbe Strahlenstärke; bleibt sie sechs Sekunden darunter, tritt ein statisches Bild an die Stelle der Leinwand. `?noguard` schaltet beides ab.

**Bei `prefers-reduced-motion`** verschwindet die Leinwand ganz und die fünf Akte stehen als ruhig gesetzte Zeilen untereinander. Ohne JavaScript ebenso — die WebGL-Schicht ist additiv, die Seite darunter ist vollständig.

**Alle vier Sprachen** sind auch hier vollständig übersetzt, inklusive der Marken am Lineal rechts (`Auszug / Licht / Satz / Zustellung`).

## Der Deploy-Ordner (`dist/`)

`python3 deploy.py` baut aus `versions/bold/index.html` den fertigen Ordner, den du hochlädst. Vorher muss `python3 assets.py` einmal gelaufen sein (Favicon und Vorschaubilder); die Schriften liegen bereits in `dist/fonts/`.

```
dist/
  index.html          Deutsch
  fr/  it/  en/      je index.html, vollständig vorgerendert
  impressum/          Entwurf, mit markierten Platzhaltern
  datenschutz/        Entwurf, mit markierten Platzhaltern
  fonts/  fonts.css   Source Serif 4 und IBM Plex Mono, latin + latin-ext
  favicon.svg .ico    das T aus der Wortmarke, als echter Pfad
  apple-touch-icon.png  icon-192.png  icon-512.png  site.webmanifest
  og-de|fr|it|en.png      Vorschaubilder, 1200 × 630
  robots.txt  sitemap.xml
```

Hochladen: der ganze Inhalt von `dist/` nach `httpdocs/`. Kein Build-Schritt auf dem Server, keine Datenbank, kein Node.

**Vier echte Adressen statt `?lang=`.** Jede Sprache ist eine eigene Datei mit eigenem `lang`, eigenem Titel, eigener Beschreibung, eigenem `canonical` und eigenem Vorschaubild; alle vier verweisen per `hreflang` aufeinander. Der Text ist vorgerendert — die Seite ist damit auch ohne JavaScript in vier Sprachen vollständig lesbar, und die Sprachwahl in der Kopfzeile sind jetzt Links, keine Knöpfe. Alte Links mit `?lang=xx` funktionieren weiterhin und schalten im Browser um.

**Was dabei bewusst wegfällt:** die automatische Spracherkennung nach Browsereinstellung. `tellingly.ch/` liefert jetzt immer Deutsch. Das ist Absicht — eine Startseite, die je nach Besucher eine andere Sprache zeigt, verwirrt Suchmaschinen (der Googlebot kommt mit englischer Spracheinstellung und würde unter der deutschen Adresse die englische Fassung sehen). Wenn du willst, baue ich stattdessen einen schmalen, wegklickbaren Hinweis ein: «This page is also available in English».

**Schriften kommen vom eigenen Server.** Kein Aufruf bei Google Fonts mehr, also keine Datenübermittlung in die USA beim blossen Seitenaufruf — und ein Grund weniger, im Datenschutztext etwas erklären zu müssen. Nur die Subsets `latin` und `latin-ext`, das deckt alle vier Sprachen ab. Source Serif 4 ist eine variable Schrift, deshalb reicht eine Datei für alle Schnitte.

**Das Zeichen ist typografisch, nicht erfunden:** ein T aus Source Serif 4 Semibold, als Pfad aus der Schrift geschnitten. Das SVG-Favicon dreht sich in dunklen Browserleisten um, damit es in beiden Fällen sichtbar bleibt.

**Die Rechtstexte sind Entwürfe.** Jeder Platzhalter ist im Text farbig markiert: Sitz, UID, Handelsregistereintrag, vertretungsberechtigte Person, Gerichtsstand, Hoster, Serverstandort und Aufbewahrungsfrist der Logfiles. Sie stehen bewusst nur auf Deutsch — fünf Übersetzungen eines ungeprüften Rechtstexts sind verschwendete Arbeit. Sobald du die deutsche Fassung freigegeben hast, übersetze ich sie.

Der Datenschutztext behauptet nichts, was die Seite nicht einhält: keine Cookies, kein `localStorage`, keine Analyse, keine Einbindungen Dritter. Ich habe die gebaute Datei darauf geprüft — der einzige ausgehende Verweis ist der Beispiel-Link in der Formate-Sektion.

## Offen — bitte prüfen

1. **Der externe Beispiel-Link ist entfernt.** In der Brief-Vorschau stand «Portfolio Brief live ansehen» und öffnete `migro.chatty-pal.com`. Markup, Stil und der Schlüssel `fmt.brief.link` sind raus; die Formate-Sektion trägt sich ohne ihn. Wenn es später eine eigene Demo-Adresse gibt, baue ich den Link an derselben Stelle wieder ein.
2. **Polnisch ist entfernt.** Auf Wunsch: Sprachwahl, Übersetzungen, Demo-Inhalte, Akte der Prolog- und 3D-Fassung, Vorschaubild und Sitemap-Eintrag. Der Stand ist wiederherstellbar — `build.py.bak6` trägt die fünfsprachige Fassung.
3. **Zahlen in der Vorschau.** «−3.12 %», «Ihr Jahr in dreissig Sekunden» und «Was Ihr Portfolio bewegte» stammen aus deiner laufenden Demo, nicht aus einer Erfindung. Wenn sich die Demo ändert, sollten die drei Bausteine mitziehen.
3. **`hallo@tellingly.ch` ist ein Platzhalter.** Die Adresse ist zweimal in `index.html` hinterlegt (Button und Textzeile) plus im Script bei `mailto:`. Bitte durch die echte ersetzen.
4. **Wortmarke.** Typografisch gesetzt (Source Serif 4, Semibold), kein Signet — wie gewünscht nichts erfunden.
5. **Hero-Hintergrund.** Alle fünf Dokumente sind plausibel konstruiert, nicht real — inklusive Wertschriften, Noten, Laborwerten und Beurteilungsstufen. Die Kopfzeilen sind bewusst zweisprachig DE/FR gesetzt, wie es Schweizer Formulare oft sind; deshalb bleiben sie in allen Sprachfassungen gleich.
7. **Demo-Inhalte sind erfunden.** Die fünfzehn Rückblicke sind plausibel konstruiert: Depotwerte, Altersguthaben, Noten, Laborwerte, Zielerreichungen. Struktur und Ton folgen deiner laufenden Portfolio-Demo, die Zahlen nicht. Sobald es echte, freigegebene Muster gibt, gehören sie hier hinein.
8. **Gesundheitsdemo.** Der Health-Rückblick nennt HbA1c und LDL mit erklärendem Text. Das ist eine Produktdemonstration, keine medizinische Aussage. Für einen echten Kunden gehört der Text von dessen Ärzteschaft, nicht von uns.
9. **Rechtsform.** Die Seite spricht als bestehende Firma: die Fusszeile sagt «Tellingly GmbH — Kreuzlingen, Schweiz», in allen vier Sprachen (`foot.legal`). Kein Satz auf der Seite sagt mehr, dass die Gründung noch bevorsteht oder dass erst Partner gesucht werden. Prüfe vor dem Livegang, dass die Eintragung im Handelsregister tatsächlich erfolgt ist — «GmbH» im Impressum einer nicht eingetragenen Firma ist in der Schweiz heikel.
10. **Impressum/Datenschutz** liegen als Entwurf in `dist/` — Platzhalter ersetzen und juristisch gegenlesen lassen.
13. **TLS.** `tellingly.ch` löst bereits auf Hostpoint auf, das Zertifikat gilt aber noch nicht für die Domain. Im Hostpoint-Panel Let's Encrypt aktivieren, bevor die Seite live geht.
11. **Keine Über-uns-Sektion.** Auf Wunsch entfernt: die Navigation führt jetzt Argument, Formate, Bereiche, Ausprobieren, Kontakt. Die Wortherkunft («in a telling manner») steht damit nirgends mehr auf der Seite — falls sie zurück soll, gehört sie eher in den Kontaktabschnitt als in eine eigene Sektion.
