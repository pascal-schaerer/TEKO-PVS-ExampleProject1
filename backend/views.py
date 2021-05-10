from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .serializer import ContactSerializer, ContactCreateSerializer, AddressSerializer
from .models import Contact, Address

class ContactApiView(ModelViewSet):
    queryset = Contact.objects.all()

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return ContactCreateSerializer
        return ContactSerializer

class AddressApiView(ModelViewSet):


    serializer_class = AddressSerializer
    queryset = Address.objects.all()