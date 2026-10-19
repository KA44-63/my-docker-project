# OCI Docker HTML Generator

Проект сгенерированного HTML-сайта, запакованного в OCI-совместимый Docker-образ на базе Nginx.

## Структура проекта
- generate.py — Python-скрипт, генерирующий index.html.
- Dockerfile — Multi-stage сборка (Python для генерации + Nginx Alpine для раздачи HTML).

## Запуск проекта

### 1. Сборка Docker-образа
\\\ash
docker build -t my-html-app:v1 .
\\\

### 2. Запуск контейнера
\\\ash
docker run -d -p 8080:80 --name my-container my-html-app:v1
\\\

После запуска откройте [http://localhost:8080](http://localhost:8080) в браузере.