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