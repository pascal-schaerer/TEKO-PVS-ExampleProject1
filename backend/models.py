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
