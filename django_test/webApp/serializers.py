from rest_framework import serializers
from .models import Customer, PaymentCustomer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class PaymentCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentCustomer
        fields = '__all__'