# test_task

## Установка:
Для развертывания вирт. окружения:
~~~
python3 -m venv venv
~~~
Активация вирт. окружения:
~~~
source venv/bin/activate # для Linux
source venv/Scripts/activate # для Windows
~~~
Установка зависимостей:
~~~
pip install -r requirements.txt
~~~

Заходим в рабочую папку:
~~~
cd .. tree_menu
~~~

Подготавливаем и применяем миграции:
~~~
python3 manage.py makemigrations
python3 manage.py migrate
~~~

Создаем суперюзера:
~~~
python3 manage.py createsuperuser
~~~

Запускаем проект:
~~~
python3 manage.py runserver
~~~

Создаем категории и проверяем работу
