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


# Address Model
class Address(models.Model):
    street = models.CharField(max_length=256)
    zip = models.CharField(max_length=10)
    city = models.CharField(max_length=256)
    country = models.CharField(max_length=2)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
