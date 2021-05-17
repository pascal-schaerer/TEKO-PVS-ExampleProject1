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
class Address
```
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
```

### Installiere Django Restframework
```
pipenv install djangorestframework
```

### Registriere Django Restframework
Add in settings.py 
```
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

### Serializer hinzufügen
Add file serializer.py to backend folder
```
from rest_framework.serializers import ModelSerializer

from .models import Contact, Address

class ContactSerializer(ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'

class AddressSerializer(ModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'
```

### View definieren
Add in backend/views.py
```
from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .serializer import ContactSerializer, AddressSerializer
from .models import Contact, Address

class ContactApiView(ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class AddressApiView(ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
```

### Routen definieren
Registrieren der backend Routen in example_project/urls.py (include inkludieren nicht vergessen :) )
```
...
from django.urls import path, include
...

urlpatterns = [
    ...
    path('api/v1/', include('backend.urls')),
    ...
]
```

Add file urls.py to backend
```
from rest_framework.routers import DefaultRouter

from .views import ContactApiView, AddressApiView

router = DefaultRouter()
router.register('contacts', ContactApiView)
router.register('addresses', AddressApiView)

urlpatterns = router.urls
```

# Workflow Aufgabe 3

## Implementiere unter /api/v1/doc die Rest Api Dokumentation ReDoc

### Library installieren

```
pipenv install drf-yasg 
```

### Library registrieren
in settings.py add

```
INSTALLED_APPS = [
    ...
    'drf_yasg',
    ...
```

### Url definieren
in urls.py

```
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

schema_view = get_schema_view(
   openapi.Info(
      title="Contact DB API",
      default_version='v1',
      description="School project",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

...

urlpatterns = [
...
    path('api/v1/doc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-ui'),
...
```

##  Integriere Django Filters und aktiviere das Filtering von dem Feld Type im Model Contact

### Installiere Library

```
pipenv install django-filter
```

### Registriere App

```
INSTALLED_APPS = [
    ...
    'django_filters',
    ...
]
```

### Erstelle den Filter für Feld 'type' im Contact
in backend/views.py
```
...
from django_filters.rest_framework import DjangoFilterBackend
...

class ContactApiView(ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type',]

```

## Aktivere die Suche auf dem Endpoint contacts. Integriere die Felder Name, First_name
in backend/views.py -> filters importieren, Searchfilters den filters_backends hinzufügen, search_fields definieren

```
...
from rest_framework import filters
...

class ContactApiView(ModelViewSet):
...
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name','first_name']
```


