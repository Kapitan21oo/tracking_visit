# tracking_visit
## Веерсии:
- Python = 3.9
- Django = 4.2.6
- djangorestframework = 3.14.0

### Порядок установки
- Клонируйте репозиторий:
  - git clone https://github.com/Kapitan21/tracking_visit.git
- Создайте виртуальное окружение
    - python -m venv venv
- Активируйте виртаульное окружение
  - .\venv\Scripts\activate (Для windows)
  - source venv/bin/activate (Для macOS/Linux)
- Установите зависимости:
  - pip install -r requirements.txt
- Настройте базу данных PostgreSQL
  - 1. Зайдите в файл  main_project/main_project/settings.py
    2. Найдите строку 67, где написанно DATABASES = KEY_DB и за мените **KEY_DB** на:


       {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'навзание базы данных',
        'USER': 'ваш юзер базы данных',
        'PASSWORD': 'ваш пароль от базы данных',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}

Заменить **NAME**, **USER**, **PASSWORD** на фактические значения вашей базы данных


- Примените миграции:
  - python manage.py migarte
- Создайте суперпользователя:
    - python manage.py createsuperuser
- Запустите сервер:
    - python manage.py runserver
### 





