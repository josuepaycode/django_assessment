
from rest_framework import serializers
from webApp.models import Customer, PaymentCustomer


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Customer
        fields = '__all__'
        #exclude = ('user',)


class PaymentCustomerSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = PaymentCustomer
        fields = '__all__'
        #exclude = ('user',)
