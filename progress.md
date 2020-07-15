# version 1.0.0 - 12 JUNE 2020

> terminal command
- work in repo
**folder/file**

## setup
> $ mkdir foodie-journal

Use poetry to initialize folder 

> $ cd `foodie-journal` 
> $ poetry init -n 
> $ poetry add 
        python = "^3.8"
        djangorestframework = "^3.11.0"
        django = "^3.0.8"
        gunicorn = "^20.0.4"
        whitenoise = "^5.1.0"
        django-cors-headers = "^3.4.0"
        django-environ = "^0.4.5"
        psycopg2-binary = "^2.8.5"
        djangorestframework-simplejwt = "^4.4.0"
> $ poetry shell 

> $ django-admin startproject journal_api_project .
> $ python manage.py startapp recipes

touch **Dockerfile**
touch **docker-compose.yml**
touch **requirements.txt**
> $ poetry export -f requirements.txt -o requirements.txt

> $ docker-compose up -d

**pyproject.toml**
```python = "~3.8"```
> $ poetry add djangorestframework-simplejwt

**recipes/models.py**
- class Recipe

**recipes/admin.py**
- register Recipe

touch **recipes/permissions.py**
- read only for view write only for author

touch **recipes/serializers.py**

**recipes/views.py**
- import model, serializer, permissions
- list and detail view

**recipes/urls.py**
- home  =  list
- int   =  detail

**project/settings.py**
- convert to future env
- installed apps
- middleware
- databases

**project/urls.py**
- import jwt
- app urls
- authorization - token - token refresh

**recipes.tests.py**
- basic content test

made superuser


#############   NOT DONE YET  ############

 SQLite >> PostgreSQL
**db.sqlite3**
 ElephantSQL


touch **project/.env** *INSIDE PROJECT FOLDER*

move settings to env
- rebuild after moving to env
> $ docker compose down 
> $ docker compose up --build - d

collect static files *INSIDE CONTAINER*
touch empty **static/** folder
    collect static needs static folder to create **staticfiles** folder


httpie
> $ http POST :8000/api/token/ username=griffin password=12345

> $ http :8000/api/v1/ "Authorization: Bearer <'paste token'>"

postman website

superuser cannot see without token 
**library/settings**
```      'rest_framework.authentication.SessionAuthentication',
      'rest_framework.authentication.BasicAuthentication',
```
now the superuser can see without token
  browsable api (see without using django admin)





deploy through heroku or AWS -- tbd
next.js app will use live link ^^


deploy next through vercel


vercel errors: python and js allow, but connecting uses others that do not allow
    Link import 'next/Link' must be /link
        X import Link from 'next/Link'
        √ import Link form 'next/link'
                                 ^



