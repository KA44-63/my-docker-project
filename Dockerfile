FROM python:3.11-slim AS builder
WORKDIR /app
COPY generate.py .
RUN python generate.py

FROM nginx:alpine
COPY --from=builder /app/index.html /usr/share/nginx/html/index.html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
