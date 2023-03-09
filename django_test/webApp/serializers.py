from django.db.models import fields
from rest_framework import serializers
from .models import Customer, CustomerPayment

class CustomerSerializer(serializers.ModelSerializer):
    """Customer Serializer"""
    class Meta:
        """Meta"""
        model = Customer
        fields = ('id', 'name', 'paternal_surname', 'email')

class CustomerPaymentSerializer(serializers.ModelSerializer):
    """Customer Payment Serializer"""
    class Meta:
        """Meta"""
        model = CustomerPayment
        fields = ('amount', 'product_name', 'quantity')
