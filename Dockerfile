FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Устанавливаем Node.js для сборки фронтенда
RUN apt-get update && apt-get install -y \
    curl \
    && curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Копируем скрипт сборки фронтенда
COPY scripts/build_frontend.sh /app/build_frontend.sh
RUN chmod +x /app/build_frontend.sh

# Устанавливаем зависимости Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && adduser --disabled-password appuser

# Копируем код приложения и фронтенда
COPY app app
COPY frontend frontend

# Собираем фронтенд
RUN /app/build_frontend.sh

# Меняем владельца файлов
RUN chown -R appuser:appuser /app

USER appuser

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
