from rest_framework import serializers
from .models import *

class contact_serializer(serializers.ModelSerializer):
    class Meta:
        model=contact
        fields=['id','phoneNumber','email','linkedId']

class id_serializer(serializers.ModelSerializer):
    class Meta:
        model=contact
        fields=['id']