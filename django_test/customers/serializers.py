from rest_framework.serializers import ModelSerializer

from .models import Customer


class CustomerModelSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            "id",
            "name",
            "paternal_surname",
            "email",
        )

        read_only_fields = (
            "id",
        )
