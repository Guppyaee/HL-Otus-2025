HL-Otus-2025: Социальная сеть (Первое ДЗ)
Описание
Серверное приложение, реализующее на Flask и PostgreSQL регистрацию, авторизацию и просмотр анкет пользователей.

Как запустить проект локально
1. Клонируйте репозиторий
bash
git clone https://github.com/Guppyaee/HL-Otus-2025.git
cd HL-Otus-2025
2. Настройте и поднимите базу данных
Вариант через Docker:

bash
docker run --name pg_highload \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -e POSTGRES_USER=myuser \
  -e POSTGRES_DB=mydatabase \
  -p 5432:5432 \
  -v C:\pg_highload \
  -d postgres
Создайте структуру таблицы:

bash
psql -h localhost -U myuser -d mydatabase -f "DDL PG.sql"
3. Установите зависимости Python
bash
pip install -r requirements.txt
4. Запустите Flask приложение
bash
python app.py
По умолчанию сервер откроется на http://localhost:5000.

Пример использования через Postman
В комплекте — файл HL.postman_collection.json для быстрой проверки ручек API:

/user/register — регистрация нового пользователя

/login — авторизация (id и пароль)

/user/get/{id} — получение анкеты пользователя по UUID

Откройте файл-коллекцию в Postman, настройте параметры, отправьте тестовые запросы.

Состав репозитория
app.py — исходный код приложения Flask

DDL PG.sql — скрипт создания таблицы пользователей

HL.postman_collection.json — коллекция запросов для Postman

openapi.json — спецификация API

requirements.txt — зависимости Python

.gitignore — исключения для лишних файлов