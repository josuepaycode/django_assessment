from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import CustomerSerializer
from .models import Customer


@api_view(['GET'])
def api_overview(request):
    """API Overview"""
    api_urls = {
        'All Customers': '/customer',
        'Add customer': '/customer/create',
        'Update customer': '/customer/pk/update',
        'Delete customer': '/customer/pk/delete'
    }
    return Response(api_urls)


@api_view(['POST'])
def add_customer(request):
    """Endpoint for create customer"""
    customer = CustomerSerializer(data=request.data)

    if Customer.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if customer.is_valid() :
        customer.save()
        return Response(
            status=status.HTTP_201_CREATED,
            data=customer.data,
        )
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def view_customers(request):
    """Endpoint for list all customer"""
    customers = Customer.objects.all()

    if customers:
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)
    return Response(
        status=status.HTTP_204_NO_CONTENT,
        data=[],
    )


@api_view(['PATCH'])
def update_customer(request, pk):
    """Endpoint for update data for a specific customer"""
    customer = get_object_or_404(Customer, pk=pk)

    data = CustomerSerializer(
        instance=customer,
        data=request.data,
        partial=True,
    )

    if data.is_valid():
        data.save()
        return Response(data.data)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_customer(request, pk):
    """Endpoint for delete customer"""
    customer = get_object_or_404(Customer, pk=pk)
    customer.delete()
    return Response(status=status.HTTP_200_OK)
