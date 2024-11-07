# Docker-команда FROM вказує базовий образ контейнера
FROM python:3.12-alpine3.20

# Встановимо робочу директорію всередині контейнера
WORKDIR /app

# Встановимо системні залежності для psycopg2 та Python
RUN apk add --no-cache postgresql-dev gcc musl-dev

# Скопіюємо інші файли в робочу директорію контейнера
COPY . .

# Встановимо залежності всередині контейнера
RUN pip install -r requirements.txt

# Позначимо порт, де працює застосунок всередині контейнера
EXPOSE 8000

# Запустимо наш застосунок всередині контейнера
ENTRYPOINT ["python", "main.py"]
