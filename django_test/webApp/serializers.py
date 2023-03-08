from django.db.models import fields
from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    """Customer Serializer"""
    class Meta:
        """Meta"""
        model = Customer
        fields = ('id', 'name', 'paternal_surname', 'email')
