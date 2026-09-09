## Context

`index.html` (root, 152 KB) to monolityczna strona statyczna tellingly.ch:
- linie 23–420 + 421–634: dwa bloki `<style>` (CSS główny + CSS warstwy motion/variant)
- linie 636–1371: markup (nav z przełącznikiem języków, sekcje argument/formats/verticals/try/who/contact)
- linie 1372–2030: skrypt 1 — słownik i18n (de/fr/it/en) + logika (przełączanie języka, combo/selektory, kontakt)
- linie 2031–2288: skrypt 2 — warstwa motion (progress bar, animacje) — addytywna, strona działa bez niej
- fonty: Google Fonts CDN (IBM Plex Mono, Source Serif 4)

W `dist/` istnieje już build wielojęzyczny z lokalnymi fontami (`dist/fonts/*.woff2`, `dist/fonts.css`) — stąd pobierzemy fonty i `fonts.css`, nie będąc zależnym od CDN.

Ograniczenia: czysto statyczna strona, brak backendu, strona ma zachowywać się identycznie jak oryginał (ten sam URL `/`, te same ankiery, i18n przez `?lang=` i przełącznik).

## Goals / Non-Goals

**Goals:**
- Podział monolitu na `web/index.html`, `web/css/*.css`, `web/js/*.js` bez zmian zachowania.
- Lokalne fonty (zero zależności od Google Fonts CDN).
- Wdrożenie jednym poleceniem: `docker compose up` → nginx serwuje `web/` na porcie 8080.
- Produkcyjne nagłówki (cache, bezpieczeństwo, kompresja).

**Non-Goals:**
- Nie ruszamy `source/*.py`, `dist/`, `versions/` — to osobny pipeline builda.
- Brak backendu, API, bazy danych, CI/CD, HTTPS w koncie (SSL to warstwa reverse-proxy, nie kontenera).
- Nie rozbudowujemy strony o nowe funkcje — tylko refaktoryzacja strukturalna.

## Decisions

1. **Struktura `web/` jako katalogu wdrażanego** (zamiast nadpisywania root `index.html`).
   - *Dlaczego:* monolityczny `index.html` zostaje jako artefakt źródłowy; `web/` jest dokładnie tym, co trafia do kontenera. Zero ryzyka utraty oryginału.
   - *Alternatywa:* nadpisanie root `index.html` + pliki obok — odrzucone, miesza "źródło" z "buildem".

2. **Podział JS na 2 pliki zgodny z granicą w oryginale:**
   - `js/i18n.js` — słownik tłumczeń + mechanizm przełączania języka (odpowiednik skryptu 1),
   - `js/motion.js` — warstwa animacji (odpowiednik skryptu 2), z zachowaniem zasady: strona działa bez niego.
   - *Dlaczego 2 a nie 1:* granica w oryginale jest wyraźna (komentarz "VARIANT B — motion layer... page works with this script removed"). Ładowanie: `i18n.js` z `defer` przed `</body>`, `motion.js` z `defer` po nim.
   - *Alternatywa:* jeden `app.js` — odrzucone, traci czytelność granicy i możliwość wyłączenia motion.

3. **CSS w 2 plikach: `css/main.css` + `css/motion.css`** (1:1 z dwoma blokami `<style>`). Ładujemy oba; `motion.css` zawiera style warstwy animacji.
   - *Alternatywa:* jeden złączony `main.css` — odrzucone, gorsza czytelność i diff'owalność względem oryginału.

4. **Fonty lokalne z `dist/`:** kopiujemy `dist/fonts/` → `web/fonts/` oraz `dist/fonts.css` → `web/css/fonts.css`, usuwamy `<link>` do Google Fonts.
   - *Dlaczego:* brak zewnętrznego CDN = szybszy first paint, brak zależności sieciowej, pełna offline-owność kontenera.
   - *Alternatywa:* zostawienie CDN + `preconnect` — odrzucone, "bardziej produkcyjnie" = zero zewnętrznych zależności.

5. **nginx:alpine jako serwer** (zamiast caddy/node/express).
   - *Dlaczego:* najlżejszy sensowny serwer do czysto statycznej strony; brotli/gzip, cache, nagłówki — wszystko w konfiguracji, zero kodu.
   - *Alternatywa:* `caddy:2` (automatyczny HTTPS) — odrzucone, SSL i tak jest za reverse proxy; `node` — odrzucone, overkill.

6. **Konfiguracja nginx w `deploy/nginx.conf`** (nie nadpisywanie `nginx.conf` bazowego):
   - `gzip` dla html/css/js/svg/json/xml, `gzip_min_length 1024`;
   - `expires 30d` + `Cache-Control: public, immutable` dla `/fonts/`, `/css/`, `/js/`, ikon; `no-cache` dla HTML;
   - nagłówki bezpieczeństwa: `X-Content-Type-Options: nosniff`, `X-Frame-Options: SAMEORIGIN`, `Referrer-Policy: strict-origin-when-cross-origin`, `Permissions-Policy`;
   - `try_files $uri $uri/ =404`, `charset utf-8`, `server_tokens off`.
   - *Alternatywa:* brotli modułem — odrzucone, wymaga buildu customowego obrazu; gzip wystarcza.

7. **Port 8080:80** w compose (nie 80, żeby nie konfliktować z lokalnymi usługami).

8. **Tagowanie assetów bez hasha** (nazwy stabilne: `main.css`, `i18n.js`).
   - *Dlaczego:* strona ma 6 assetów, wdrożenie = nowy kontener; `no-cache` dla HTML + 30 dni dla assetów to wystarczający model. Hashy nazw wymagałyby build pipeline'u, którego nie ma.
   - *Trade-off:* przy aktualizacji assetów z cache 30d — akceptowalne (sitemap/firmy tego typu wdrażają rzadko; można krótko obniżyć TTL).

## Risks / Trade-offs

- [Rozbicie inline→pliki zmieni kolejność/blokowanie rendera] → CSS w `<head>` (blokujący, jak w oryginale — zachowujemy), JS z `defer` na końcu body; weryfikacja porównaniem zachowania (i18n, ankiery, combo).
- [Ręczne kopiowanie 600 linii CSS/800 linii JS = błąd przepisu] → kopiujemy dosłownie (sed/range z oryginału), potem diff semantyczny: render oryginału vs `web/` w browserze + test i18n (zmiana `?lang=` na wszystkie 4 języki).
- [Fonty z `dist/` mogą nie pokrywać wszystkich subsetów (latin-ext)] → weryfikacja: porównać listę plików `fonts.css` z tymi używanymi; pliki latin + latin-ext są w `dist/fonts/` (8 plików).
- [`immutable` + 30d na assety może utrudnić hotfix] → w razie hotfixu: krótki `Cache-Control` w nagłówku lub zmiana nazwy pliku; udokumentowane w README.

## Migration Plan

1. Zbudować `web/` z rozbitego oryginału, zweryfikować lokalnie (`python3 -m http.server` / `docker compose up`).
2. Porównanie rendera: oryginał vs `web/` (visually + i18n + ankiery + combo).
3. `docker compose up -d` → curl checki (statusy, nagłówki cache, kompresja, 404).
4. Rollback: usunąć `web/` + pliki Docker — root `index.html` zostaje nietknięty, zero regresji.

## Open Questions

(brak — zakres zamknięty decyzjami wyżej)
