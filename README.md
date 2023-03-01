# FOODGRAM
## Дипломная работа после прохождения курса Python-разработчик в Яндекс.Практикум

сайт работает по адресу http://158.160.61.133/
логин admin@ex.com
пароль admin

Технологии:

* python 3.10
* django 2.2.19

Для запуска в режиме разработки необходимо:

1. Клонировать с github
2. Создать виртуальное окружение  `python -m venv venv`
3. Активировать виртуальное окружение `source venv/Scripts/activate`
4. Обновить менеджер пакетов pip `python -m pip install --upgrade pip`
5. Установить зависимости `pip install -r requirements.txt`

...

Для запуска на удаленном сервере:
1. Добавить ваш публичный SSH-ключ на сервер `cat ~/.ssh/id_rsa.pub`
2. Подключиться к удаленному серверу `ssh your_login@pu.bl.ic.ip`
3. Обновить индекс пакетов APT `sudo apt update`
4. Обновите установленные в системе пакеты и установите обновления безопасности `sudo apt upgrade -y `
5. Установиь pip venv git `sudo apt install python3-pip python3-venv git -y`
6. Сгенерировать SSH-ключ `ssh-keygen -t rsa` для клонирования
7. Отредактировать setting: ALLOWED_HOSTS = ['xxx.xxx.xxx.xxx', '127.0.0.1', 'localhost'] — IP вашего сервера
8. Отключите «режим разработки»
9. ...
10. для загрузки ингредиентов: `python manage.py load_ingredients`

