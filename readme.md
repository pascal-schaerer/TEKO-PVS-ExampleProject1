# Workflow

## Projekt erstellen

### Python environment erstellen

```
pipenv shell
```

### Django Framework installieren

```
pipenv install Django
```

### Django Projekt erstellen

```
django-admin startproject example_project .
```

### Python Interpreter selektieren
Run and Debug -> crtl+shift+p -> Select Python Interpreter -> Python 3.9.44 64-bit ('example_project': pipenv)

### launch.json erstellen
Run and Debug -> create a launch.json file -> Python -> Django

### Django starten
Run

### App hinzufügen

```
python manage.py startapp backend
```

### App registrieren
example_project\settings.py -> backend in INSTALLED_APPS hinzufügen

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'backend',
]
```

### Models definieren
backend/models.py

```
from django.db import models

# Contact Model
class Contact(models.Model):
    type = (
        ('private'),
        ('business'),
    )
    name = models.CharField(max_length=256)
    first_name = models.CharField(max_length=256)

    addresses = models.ManyToManyField('Address', related_name='contacts')

# Address Model
class Address(models.Model):
    street = models.CharField(max_length=256)
    zip = models.CharField(max_length=10)
    city = models.CharField(max_length=256)
    country = models.CharField(max_length=2)
```

#### Änderungen migrieren
```
python manage.py makemigrations
python manage.py migrate
```