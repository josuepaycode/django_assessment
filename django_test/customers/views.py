from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import CustomerModelSerializer
from .models import Customer


class CustomerModelViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name", "email"]
