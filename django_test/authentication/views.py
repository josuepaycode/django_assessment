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


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    admin = authenticate(username=email, password=password)

    if admin:
        return Response(data={'token':admin.token})
    return Response(
        {'message': 'Invalid credentials'},
        status=status.HTTP_401_UNAUTHORIZED,
    )
