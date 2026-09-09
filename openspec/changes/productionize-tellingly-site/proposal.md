## Why

Strona Tellingly istnieje jako jeden monolityczny plik `index.html` (152 KB: 2 bloki CSS inline, 2 skrypty inline, zależności od Google Fonts CDN). Taki format utrudnia cache'owanie, przeglądanie zmian i wdrożenia. Nie ma też żadnej warstwy serwowania — nie ma Dockerfile ani konfiguracji nginx.

## What Changes

- Rozbicie `index.html` na osobne pliki: `index.html` (czysty markup), `css/main.css`, `css/motion.css`, `js/i18n.js` (słownik tłumczeń + przełączanie języka + logika strony), `js/motion.js` (warstwa motion, addytywna).
- Lokalizacja fontów: kopiowanie woff2 z `dist/fonts/` + `fonts.css`, usunięcie zależności od Google Fonts CDN.
- Produkcyjna statyczna struktura `web/` (index, css, js, fonts, ikony, robots.txt, sitemap.xml).
- Konteneryzacja: `Dockerfile` (nginx:alpine), `docker-compose.yml`, dedykowany `nginx.conf` z kompresją gzip, cache'owaniem assetów, nagłówkami bezpieczeństwa i trybem try-catch 404.
- Oryginalny monolityczny `index.html` pozostaje w repo jako artefakt źródłowy (bez zmian); nowa struktura trafia do `web/`.

## Capabilities

### New Capabilities

- `site-structure`: statyczna, podzielona struktura strony (HTML/CSS/JS/fonty) zachowująca pełną funkcjonalność oryginału (i18n de/fr/it/en, sekcje, interakcje, motion layer).
- `container-deployment`: wdrażanie strony w kontenerze nginx z docker compose, kompresją, cache i nagłówkami bezpieczeństwa.

### Modified Capabilities

(brak — to pierwszy spec w projekcie)

## Impact

- Nowe pliki: `web/**`, `Dockerfile`, `docker-compose.yml`, `deploy/nginx.conf`, `.dockerignore`.
- Żadnych zmian w `source/*.py`, `dist/`, `versions/`.
- Brak API, baz danych ani backendu — czysto statyczny serwis.
