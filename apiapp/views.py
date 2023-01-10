from django.shortcuts import render

# Create your views here.
from customers.models import customers
from payments.models import payments
from django.contrib.auth.models import User, Group

from rest_framework import viewsets, permissions,status
from .serializers import customerSerializer,paymentSerializer,userSerializer,groupSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

class customerViewSet(viewsets.ModelViewSet):
    queryset=customers.objects.all()
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=customerSerializer

class paymentsViewSet(viewsets.ModelViewSet):
    queryset=payments.objects.all()
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=paymentSerializer

class userViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=userSerializer
    permission_classes=[permissions.IsAuthenticated]

class groupViewSet(viewsets.ModelViewSet):
    queryset=Group.objects.all()
    serializer_class=groupSerializer
    permission_classes=[permissions.IsAuthenticated]

