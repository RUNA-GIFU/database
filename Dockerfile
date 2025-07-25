# backend/Dockerfile (Django用)
FROM python:3.9-slim-buster # DjangoはPython上で動作

WORKDIR /app

# Pythonの依存関係ファイルをコピーしてインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Djangoプロジェクトのコードをコピー
COPY . .

# Djangoがリッスンするポート
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]