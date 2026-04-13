FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Створюємо папку storage (якщо не існує)
RUN mkdir -p storage && \
    echo "{}" > storage/data.json

EXPOSE 3000

CMD ["python", "app.py"]
