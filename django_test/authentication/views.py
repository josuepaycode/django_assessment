from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AdministratorSerializer


@api_view(['POST'])
def create_auth_admin(request):
    """Endpoint for create Administrator"""
    admin = AdministratorSerializer(data=request.data)

    admin.is_valid(raise_exception=True)
    admin.save()
    return Response(
        status=status.HTTP_201_CREATED,
        data=admin.data,
    )
