# OCI Docker HTML Генераторы

Жоба Python арқылы HTML парақшасын генерациялап, оны Nginx базисіндегі OCI-үйлесімді Docker-образға жинақтайды.

## Жоба құрылымы
- generate.py — index.html файлын генерациялайтын Python скрипті.
- Dockerfile — Multi-stage жинақтау (Python арқылы HTML жасау + Nginx Alpine арқылы тарату).
- .github/workflows/build.yml — GitHub Actions арқылы Docker-образды автоматты түрде жинақтау және GHCR-ге жүктеу (CI/CD).

## Жобаны іске қосу

### 1. Docker-образды локальды түрде жинақтау
docker build -t my-html-app:v1 .

### 2. Контейнерді іске қосу
docker run -d -p 8080:80 --name my-container my-html-app:v1

Браузерде ашу: http://localhost:8080

---

## GitHub Container Registry (GHCR) арқылы дайын образды жүктеу

Сондай-ақ, GitHub Actions автоматты түрде жинақтаған дайын OCI-образды бір командамен іске қосуға болады:

docker run -d -p 8080:80 ghcr.io/ka44-63/my-docker-project:latest