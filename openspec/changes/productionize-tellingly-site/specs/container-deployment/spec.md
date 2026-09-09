## ADDED Requirements

### Requirement: Wdrożenie kontenerowe jednym poleceniem
Projekt SHALL dostarczać `Dockerfile` (bazujący na `nginx:alpine`) i `docker-compose.yml`, tak aby `docker compose up -d` wystawiło stronę z `web/` na porcie hosta 8080 (mapowanie 8080:80).

#### Scenario: Build obrazu
- **WHEN** wywołany jest `docker build` z katalogu root projektu
- **THEN** obraz buduje się bez błędów i `.dockerignore` wyklucza z contextu `dist/`, `versions/`, `source/`, `_transfer.tar.gz`, `.git`

#### Scenario: Start kontenera
- **WHEN** wywołany jest `docker compose up -d`
- **THEN** kontener nginx startuje i nasłuchuje na porcie 8080 hosta

#### Scenario: Strona dostępna pod /
- **WHEN** wykonany jest `GET /`
- **THEN** odpowiedź ma status 200, `Content-Type: text/html` i zawiera markup Tellingly z odwołaniami do `css/` i `js/`

### Requirement: Serwowanie assetów z cache'owaniem i kompresją
nginx SHALL serwować assety (`/css/`, `/js/`, `/fonts/`, ikony) z nagłówkami `Cache-Control: public, max-age=2592000, immutable`, a pliki HTML z `Cache-Control: no-cache`. Odpowiedzi tekstowe (html, css, js, svg, json, xml, woff2) SHALL być kompresowane gzip dla odpowiedzi >1024 bajtów.

#### Scenario: Cache na fonty
- **WHEN** wykonany jest `GET /fonts/source-serif-4-400-normal-latin.woff2`
- **THEN** nagłówek `Cache-Control` zawiera `max-age=2592000` i `immutable`

#### Scenario: HTML bez cache
- **WHEN** wykonany jest `GET /`
- **THEN** nagłówek `Cache-Control` zawiera `no-cache`

#### Scenario: Kompresja gzip
- **WHEN** wykonane jest `GET /css/main.css` z nagłówkiem `Accept-Encoding: gzip`
- **THEN** odpowiedź ma `Content-Encoding: gzip` i mniejszą rozmiarem niż wersja skompresowana

#### Scenario: 404 dla brakujących ścieżek
- **WHEN** wykonany jest `GET /nie-istnieje`
- **THEN** odpowiedź ma status 404

### Requirement: Nagłówki bezpieczeństwa
nginx SHALL ustawiać na wszystkich odpowiedziach: `X-Content-Type-Options: nosniff`, `X-Frame-Options: SAMEORIGIN`, `Referrer-Policy: strict-origin-when-cross-origin` oraz ukrywać wersję serwera (`server_tokens off`).

#### Scenario: Nagłówki bezpieczeństwa obecne
- **WHEN** wykonany jest `GET /`
- **THEN** odpowiedź zawiera `X-Content-Type-Options: nosniff`, `X-Frame-Options: SAMEORIGIN` i `Referrer-Policy: strict-origin-when-cross-origin`, a nagłówek `Server` nie ujawnia wersji
