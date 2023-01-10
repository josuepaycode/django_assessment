from rest_framework import serializers
from customers.models import customers
from payments.models import payments
from django.contrib.auth.models import User,Group

class userSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=('url','username','email','groups')

class groupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields=('url','name')

class customerSerializer(serializers.ModelSerializer):
    class Meta:
        model=customers
        fields=('id_customer','nombre_cliente','apellido_cliente','correo')
        read_only_fields=('id_customer',)

class paymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=payments
        fields=('id_pago','cantidad_pago','id_cliente','producto','cantidad_producto','fecha_pago')
        read_only_fields=('id_pago','fecha_pago',)