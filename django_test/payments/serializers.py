from rest_framework.serializers import ModelSerializer

from .models import Payment


class PaymentModelSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = (
            "id",
            "amount",
            "product_name",
            "quantity",
        )

        read_only_fields = (
            "id",
        )
