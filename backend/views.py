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