from rest_framework import serializers
from authentication.models import Administrator


class AdministratorSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True,
    )
    name = serializers.CharField(max_length=250, required=False)
    role = serializers.CharField(max_length=50, required=False)

    class Meta:
        model = Administrator
        fields = ('username', 'email', 'password', 'name', 'role')

    def create(self, validated_data):
        return Administrator.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True,
    )

    class Meta:
        model = Administrator
        fields = ('email', 'password', 'token')
        read_only_fields = ['token']
