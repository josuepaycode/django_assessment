from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from common.permissions import IsSuperAdminPermission
from .serializers import PaymentModelSerializer
from .models import Payment


class PaymentModelViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["product_name",]

    def get_permissions(self):
        if self.action in ["update", "partial_update", "create", "destroy"]:
            self.permission_classes = [IsSuperAdminPermission]
        return super().get_permissions()
