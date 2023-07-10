# Documentacion de uso

## POST /answers/ inserta una respuesta en el backend
{"name":"Juan","question1":"1","question2":"2","question3":"1","question4":"1","question5":"1","question6":"1","question7":"1","question8":"1","question9":"1","question10":"2","question11":"1","question12":"2","question13":"1","question14":"1","question15":"1"}


## GET /answers/ obtiene todas las respuestas
[
  {
    "id": 1,
    "name": "Juan",
    "question1": 1,
    "question2": 2,
    "question3": 1,
    "question4": 1,
    "question5": 1,
    "question6": 1,
    "question7": 1,
    "question8": 1,
    "question9": 1,
    "question10": 2,
    "question11": 1,
    "question12": 2,
    "question13": 1,
    "question14": 1,
    "question15": 1
  }
]

## testing

super usuario : 
admin - 123patojismo1 - pgabriel@elpatojismo.edu.gt

## to render
first follow the tutorial at https://render.com/docs/deploy-django
Start since 'Update your app for production ready and follow all the steps,
import os
SECRET_KEY = os.environ.get('SECRET_KEY', default='your secret key')
DEBUG = 'RENDER' not in os.environ
https://docs.djangoproject.com/en/3.0/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
pip3 install dj-database-url psycopg2-binary
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        # Feel free to alter this value to suit your needs.
        default='postgresql://postgres:postgres@localhost:5432/mysite',
        conn_max_age=600
    )
}

pip3 install 'whitenoise'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    ...
]

STATIC_URL = '/static/'

if not DEBUG:
      STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
      STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

on build.sh

#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

and for getting that is pip freeze > requirements.txt

on the zhsch shell you do 
chmod a+x build.sh

and finaly 
pip3 install gunicorn


now on the render page you set your variables and config, first create a postgresql 
database, then create your web service, for the web service on the 
gunicorn app:app 
change it to
gunicorn < app main folder >.wsgi
and on the enviromental  variables do this

PYTHON_VERSION     XXXXX
DATABASE_URL      (go to your dataabase, scroll down and search for internal link)


aaaaaand that's it!