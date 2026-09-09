# Notes — productionize-tellingly-site

- `dist/fonts` ma tylko 8 woff2; `fonts.css` z dist/ celowo linkuje wagę 400 i 600 Source Serif 4 do plików 300-normal (skrót oryginalnego buildu). Zachowane 1:1 — render identyczny jak w dist/. Jeśli kiedyś chcemy prawdziwe 400/600: dołożyć 4 pliki (400/600 × latin/latin-ext) i poprawić 4 linie w `web/css/fonts.css`.
- `web/css/fonts.css` wymagał korekty ścieżek `url(fonts/...)` → `url(../fonts/...)`, bo CSS trafił do podkatalogu `css/`.
- Head `web/index.html` wzbogacony o linki favicon/manifest/preload fontów wzorem `dist/index.html` (oryginalny head monolitu ich nie miał).
- nginx: `add_header` nie dziedziczy między blokami location — nagłówki bezpieczeństwa powielone w każdym location (celowo, nie bug).
- HEALTHCHECK używa `wget` (busybox), nie `curl` — nginx:alpine nie ma curla (wcześniejszy kontener w logach Docker zgłaszał ten błąd).
- Docker Desktop na tej maszynie miał zombie backend od 09.02 (stary socket, VM nie startował) — wymagał `pkill -9 com.docker` + `open -a Docker`.
