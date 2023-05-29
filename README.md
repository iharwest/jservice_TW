# Веб-сервис для квизов

Веб-сервис реализован на Django с использованием REST API и PostgreSQL.
Сервис предоставляет API для получения случайных вопросов с публичного API [jService](https://jservice.io/api/random?count=1).
Полученые вопросы сохраняеются в БД. В случае, если в БД имеется такой же вопрос, к публичному API отправляются дополнительные запросы для получения уникального вопроса.

Системные требования
----------
* Python 3.7+
* Docker
* Works on Linux, Windows, macOS

## Установка

### Установка Docker.
Установите Docker, используя инструкции с официального сайта:
- для [Windows и MacOS](https://www.docker.com/products/docker-desktop)
- для [Linux](https://docs.docker.com/engine/install/ubuntu/). Отдельно потребуется установть [Docker Compose](https://docs.docker.com/compose/install/)

### Запуск проекта

Склонируйте репозиторий `git clone https://github.com/iharwest/jservice_TW.git` в текущую папку.

### Настройка проекта

Создайте ```.env``` файл в корне репозитория
Заполнить ```.env``` файл с переменными окружения по примеру:

```
      - DEBUG=1
      - DB_NAME=NAME
      - POSTGRES_USER=USER
      - POSTGRES_PASSWORD=PASSWORD
      - DB_HOST=db
      - DB_PORT=5432
      - SECRET_KEY=SECRET_KEY
```

### Сборка образов и запуск контейнеров

В корне репозитория выполните команду:

```
docker-compose up -d --build
```

### Запустите миграции:

```
docker-compose exec web python manage.py migrate
```

### Остановка контейнеров

Для остановки контейнеров выполните команду:

```
docker-compose stop
```

## Примеры запроса через Postman

Отправьте POST запрос на http://localhost:8000/question/ с телом запроса в формате JSON следующего вида:

```
{"questions_num": int}
```
В ответ придет предыдущей сохранённый вопрос для викторины. В случае его отсутствия - пустой объект.