# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем необходимые инструменты для компиляции
RUN apt-get update && \
    apt-get install -y gcc libffi-dev python3-dev cargo

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . /app/

# Устанавливаем зависимости из requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Указываем команду для запуска бота
