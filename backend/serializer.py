from rest_framework.serializers import ModelSerializer

from .models import Contact, Address

class AddressNestedSerializer(ModelSerializer):

    class Meta:
        model = Address
        fields = ['id', 'street', 'zip', 'city', 'country']

class ContactSerializer(ModelSerializer):
    addresses = AddressNestedSerializer(many=True)

    #Benötigt Model und Fields
    class Meta:
        model = Contact
        fields = ['id', 'type', 'name', 'first_name', 'addresses']

class ContactCreateSerializer(ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'

class AddressSerializer(ModelSerializer):

    class Meta:
        model = Address
        fields = ['id', 'street', 'zip', 'city', 'country']