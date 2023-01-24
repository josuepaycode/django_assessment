from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import PaymentModelSerializer
from .models import Payment


class PaymentModelViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["product_name",]
