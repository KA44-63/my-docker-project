# -*- coding: utf-8 -*-
content = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>OCI Docker HTML</title>
    <style>
        body { font-family: sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; background: #0f172a; color: #f8fafc; margin: 0; }
        .card { background: #1e293b; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.5); text-align: center; }
        h1 { color: #38bdf8; }
    </style>
</head>
<body>
    <div class="card">
        <h1>HTML успешно сгенерирован!</h1>
        <p>Образ собран по стандарту OCI и запущен в Docker.</p>
    </div>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("HTML файл успешно сгенерирован!")