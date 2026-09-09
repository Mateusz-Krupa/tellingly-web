## ADDED Requirements

### Requirement: Podzielona struktura statycznej strony
Strona SHALL być dostarczana jako katalog `web/` zawierający oddzielne pliki: `index.html`, `css/main.css`, `css/motion.css`, `css/fonts.css`, `js/i18n.js`, `js/motion.js`, `fonts/` (woff2), `robots.txt`, `sitemap.xml`, `site.webmanifest` oraz ikony. Monolityczny root `index.html` SHALL pozostać w repo nienaruszony.

#### Scenario: Wszystkie pliki struktury istnieją
- **WHEN** zbudowana jest struktura `web/`
- **THEN** `web/index.html` nie zawiera inline `<style>` ani inline `<script>` (poza ewentualnym atrybutem) i odwołuje się do `css/main.css`, `css/motion.css`, `css/fonts.css`, `js/i18n.js`, `js/motion.js`

#### Scenario: Monolityczny oryginał zachowany
- **WHEN** porównuje się root `index.html` ze stanem przed zmianą
- **THEN** plik jest byte-po-bajcie identyczny (zero modyfikacji)

### Requirement: Zachowanie funkcjonalności oryginału
Rozbita strona SHALL zachowywać się identycznie jak monolityczny oryginał: przełącznik języków de/fr/it/en (w tym przez `?lang=`), nawigacja po ankiarach, combo/selektor (vertical + format), sekcje kontakt, warstwa motion z poszanowaniem `prefers-reduced-motion`.

#### Scenario: Zmiana języka przez przełącznik
- **WHEN** użytkownik klikną język fr/it/en w nawigacji
- **THEN** wszystkie teksty z atrybutem `data-i18n` zmieniają się na wybrany język, a URL otrzymuje parametr `?lang=<kod>`

#### Scenario: Zmiana języka przez parametr URL
- **WHEN** strona jest otwarta z URL `/?lang=it`
- **THEN** strona renderuje się po włosku przy pierwszym odświeżeniu

#### Scenario: Nawigacja po ankiarach
- **WHEN** użytkownik klikna link do `#argument`, `#formats`, `#verticals`, `#try`, `#contact`
- **THEN** strona przewija się do odpowiedniej sekcji

#### Scenario: Reduced motion
- **WHEN** przeglądarka zgłasza `prefers-reduced-motion: reduce`
- **THEN** warstwa motion nie animuje elementów (zachowanie identyczne z oryginałem)

### Requirement: Lokalne fonty bez CDN
Strona SHALL używać wyłącznie lokalnych fontów (IBM Plex Mono 400/500, Source Serif 4) serwowanych z `web/fonts/` zgodnie z `fonts.css`, bez żadnych `<link>` ani `@import` do Google Fonts lub innego CDN.

#### Scenario: Brak zależności od CDN
- **WHEN** analiza `web/index.html` i wszystkich plików CSS
- **THEN** nie ma odwołań do `fonts.googleapis.com`, `fonts.gstatic.com` ani żadnego zewnętrznego originu

#### Scenario: Fonty ładują się lokalnie
- **WHEN** strona się renderuje
- **THEN** zapytania o fonty trafiają pod względny ścieżkę `/fonts/*.woff2`
