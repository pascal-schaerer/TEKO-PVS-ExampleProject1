from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .serializer import ContactSerializer, AddressSerializer
from .models import Contact, Address

from rest_framework import filters

from django_filters.rest_framework import DjangoFilterBackend

class ContactApiView(ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['type',]
    search_fields = ['name','first_name']


class AddressApiView(ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()