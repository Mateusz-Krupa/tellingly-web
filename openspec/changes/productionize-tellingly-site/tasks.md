## 1. Struktura web/ i assety statyczne

- [x] 1.1 Utworzyć katalog `web/` z podkatalogami `css/`, `js/`, `fonts/`
- [x] 1.2 Skopiować `dist/fonts/` → `web/fonts/` (wszystkie woff2) i `dist/fonts.css` → `web/css/fonts.css`
- [x] 1.3 Skopiować `dist/robots.txt`, `dist/sitemap.xml`, `dist/site.webmanifest`, `favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `icon-192.png`, `icon-512.png` → `web/` (poprawić ścieżki w webmanifest, jeśli potrzebne)

## 2. CSS

- [x] 2.1 Wyodrębnić blok `<style>` linie 23–420 root `index.html` → `web/css/main.css` (dosłownie, bez zmian)
- [x] 2.2 Wyodrębnić blok `<style>` linie 421–634 → `web/css/motion.css` (dosłownie, bez zmian)
- [x] 2.3 Zweryfikować, że `main.css` + `motion.css` łącznie zawierają dokładnie tyle samo reguł CSS co oba inline bloki (porównanie po usunięciu białych znaków)

## 3. JavaScript

- [x] 3.1 Wyodrębnić skrypt 1 (linie 1372–2030, i18n + logika) → `web/js/i18n.js` (dosłownie, bez zmian)
- [x] 3.2 Wyodrębnić skrypt 2 (linie 2031–2288, warstwa motion) → `web/js/motion.js` (dosłownie, bez zmian)
- [x] 3.3 Zweryfikować składnię obu plików (`node --check`) i że łącznie zawierają dokładnie tyle samo kodu co oba inline skrypty

## 4. index.html

- [x] 4.1 Zbudować `web/index.html` z body oryginału (linie 636–2288, bez tagów `<style>`/`<script>`) i headu z odwołaniami: `css/fonts.css`, `css/main.css`, `css/motion.css`, `js/i18n.js` (defer), `js/motion.js` (defer)
- [x] 4.2 Usunąć z headu linki do Google Fonts (preconnect + css2) i podpiąć lokalne fonty
- [x] 4.3 Zweryfikować: brak inline `<style>`/`<script>`, obecność wszystkich 5 linków (3 css, 2 js), identyczny body (diff body vs oryginał)

## 5. Docker

- [x] 5.1 Utworzyć `deploy/nginx.conf` (gzip, cache: immutable 30d dla assetów + no-cache dla HTML, nagłówki bezpieczeństwa, server_tokens off, try_files, charset utf-8)
- [x] 5.2 Utworzyć `Dockerfile` (nginx:alpine, kopiowanie `web/` → `/usr/share/nginx/html`, `deploy/nginx.conf` → `/etc/nginx/conf.d/default.conf`, EXPOSE 80, HEALTHCHECK curl /)
- [x] 5.3 Utworzyć `docker-compose.yml` (serwis `tellingly`, build z root, port 8080:80, restart unless-stopped, healthcheck)
- [x] 5.4 Utworzyć `.dockerignore` (dist, versions, source, _transfer.tar.gz, .git, .opencode, openspec, *.html poza web)

## 6. Weryfikacja

- [x] 6.1 `docker build` przechodzi bez błędów
- [x] 6.2 `docker compose up -d` → `GET /` zwraca 200 z markupiem Tellingly
- [x] 6.3 Checki nagłówków: `Cache-Control` no-cache dla `/`, immutable dla `/fonts/`, `/css/`, `/js/`; `Content-Encoding: gzip` dla CSS; nagłówki bezpieczeństwa (nosniff, SAMEORIGIN, Referrer-Policy); `GET /nie-istnieje` → 404
- [x] 6.4 Weryfikacja i18n: słownik I18N w `web/js/i18n.js` zawiera wszystkie 4 języki (de/fr/it/en), a każdy klucz `data-i18n` występujący w `web/index.html` istnieje w każdym z 4 słowników (skrypt kontrolny)
- [x] 6.5 Potwierdzić, że root `index.html` jest nietknięty (md5 vs stan początkowy) i że `dist/`, `source/`, `versions/` nie zostały zmienione
