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
