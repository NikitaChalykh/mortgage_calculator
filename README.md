REST API агрегатор и калькулятор ипотечных предложений
=====

Описание проекта
----------

Проект основан на Django Rest Framework, аутентификация в проекте не предусмотрена, настроены модели для отображения в панели администратора. 

Проект разворачивается в трех Docker контейнерах: web-приложение, postgresql-база данных и nginx-сервер. 

Реализованы тесты эндпоинтов и моделей проекта.

Реализована сортировка выходных данных API по расчитанному ежемесячному платежу и по рассчитанной ставке.

Пользовательский сценарий
----------
Клиент вводит следующие данные:
1. Стоимость объекта недвижимости, в рублях без копеек.
2. Первоначальный взнос, в рублях без копеек.
3. Срок, в годах.

В ответ клиенту приходит массив с объектами ипотечных предложений. В каждом объекте есть следующие данные:
1. Наименование банка.
2. Ипотечная ставка, в процентах.
3. Платеж по ипотеке, в рублях без копеек.

Системные требования
----------
* Python 3.8+
* Docker
* Works on Linux

Стек технологий
----------
* Python 3.8+
* Django 3.1
* PostgreSQL
* Django Rest Framework
* Nginx
* gunicorn
* Docker, Docker Compose
* unittest

Установка проекта из репозитория
----------
1. Клонировать репозиторий и перейти в него в командной строке:
```bash
git clone git@contest.idacloud.ru:Nikita223/mortgage_calculator.git

cd mortgage_calculator # Переходим в директорию с проектом
```

2. Создайте файл ```.env``` используя ```env.example``` в качестве шаблона

3. Установка и запуск приложения в контейнерах:
```bash 
docker-compose up -d
```

4. Запуск миграций, сбор статики и запуск тестов:
```bash 
docker-compose exec web python manage.py migrate

docker-compose exec web python manage.py collectstatic --no-input 

docker-compose exec web python manage.py test 
```

Работа с проектом
----------
Документация для API сервиса после установки:

```http://127.0.0.1/api/docs/```

Админка проекта:

```http://127.0.0.1/admin/```
