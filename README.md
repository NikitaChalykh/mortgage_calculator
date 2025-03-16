REST API aggregator and calculator of mortgage offers
=====

Project description
----------

The project is based on Django Rest Framework, authentication is not provided in the project, models are configured for display in the admin panel.

The project is deployed in three Docker containers: web application, postgresql database and nginx server.

Endpoint and project model tests are implemented.

Sorting of API output data by calculated monthly payment and by calculated rate is implemented.

User scenario
----------
The client enters the following data:
1. Cost of the property, in rubles without kopecks.
2. Initial payment, in rubles without kopecks.
3. Term, in years.

In response, the client receives an array with mortgage offer objects. Each object contains the following data:
1. Bank name.
2. Mortgage rate, in percent.
3. Mortgage payment, in rubles without kopecks.

System requirements
----------
* Python 3.8+
* Docker
* Works on Linux

Tech stack
----------
* Python 3.8+
* Django 3.1
* PostgreSQL
* Django Rest Framework
* Nginx
* gunicorn
* Docker, Docker Compose
* unittest

Installing the project from the repository
----------
1. Cloning the repository:
```bash
git clone git@contest.idacloud.ru:Nikita223/mortgage_calculator.git

cd mortgage_calculator # Go to the directory with the project
```

2. Create a ```.env``` file using ```env.example``` as a template in the infra folder

3. Installing and running the application in containers:
```bash
docker-compose up -d
```

4. Running migrations, collecting statics, creating a superuser and running tests:
```bash

docker compose exec web python manage.py migrate

docker compose exec web python manage.py collectstatic --no-input

docker compose exec web python manage.py createsuperuser

docker compose exec web python manage.py test
```

Working with the project
----------
Documentation on the API service:

```http://127.0.0.1/api/docs/```

Service admin panel:

```http://127.0.0.1/admin/```
