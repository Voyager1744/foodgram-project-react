# FOODGRAM - "Продуктовый помощник"
## Дипломный проект по окончанию курса Python-разработчик в Яндекс.Практикум

В этом проекте мной написаны онлайн-сервис и API для сайта "Продуктовый
помощник", а именно:

- регистрация и авторизация пользователей,
- публикация и редактирование рецептов авторизованным пользователем,
- добавление в избранное понравившегося рецепта,
- возможность подписаться на любимого автора,
- реализована фильтрация рецептов по тегам,
- добавление рецептов в корзину покупок,
- возможность скачать список ингредиентов всех рецептов добавленных в корзину.
- несколько unit-тестов



В проекте использованы следующие технологии:

* Python 3.10
* Django 2.2.19
* Django REST framework
* PostgreSQL
* NGINX
* gunicorn
* Docker
* DockerHub
* GitHub Actions
* Yandex.Cloud

Проект реализован в Docker-контейнерах, образы которых размещены на Dockerhub.

#### Для запуска на сервере необходимо:

1. Установить Docker
2. Скопировать папку _infra_ на сервер
3. Добавить в эту папку файл _.env_. Пример содержимого:

    ```
        DB_ENGINE=django.db.backends.postgresql
        DB_NAME=postgres
        POSTGRES_USER=postgres
        POSTGRES_PASSWORD=postgres
        DB_HOST=db
        DB_PORT=5432
    ```
4. В файле nginx.conf указать:

    ```nginx configuration
    server_name xxx.xxx.xxx.xxx;
    ```
   где xxx.xxx.xxx.xxx - IP адрес сервера, или _localhost_
5. Из директории _infra_ выполнить команду `sudo docker-compose up -d`
6. Последовательно выполнить следующие команды:

    ```
    sudo docker exec infra_web_1 python manage.py makemigrations
    sudo docker exec infra_web_1 python manage.py migrate
    sudo docker exec infra_web_1 python manage.py collectstatic
    # создать суперпользователя:
    sudo docker exec infra_web_1 python manage.py createsuperuser --username admin --email admin@ex.com
    ```
7. Загрузить список ингредиентов:

    ```
    sudo docker exec infra_web_1 python manage.py load_ingredients
    ```

***
Автор: [Ушаков Дмитрий](https://github.com/Voyager1744/)



