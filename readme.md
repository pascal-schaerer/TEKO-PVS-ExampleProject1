# Workflow Aufgabe 1

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
    CONTACT_TYPES = (
        ('Priv', 'private'),
        ('Busi', 'business'),
    )
    type = models.CharField(max_length=4, choices=CONTACT_TYPES)
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

### DB Superadmin erstellen
```
python manage.py createsuperuser
```

### Adminbereich konfigurieren
backend/admin.py
```
from django.contrib import admin

# Register your models here.
from .models import Contact, Address

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','type']
    list_filter = ['type']
    search_fields = ['name','first_name']

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass
```

## Open Questions
https://dev.to/bfeldman/how-to-hide-your-secret-key-in-django-16kp

# Workflow Aufgabe 2

### Ändern der Relationion zwischen Contact und Address

Remove in Class Contact
```
    addresses = models.ManyToManyField('Address', related_name='contacts')
```

Add in Class Address
class Address(models.Model):
```
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
```
