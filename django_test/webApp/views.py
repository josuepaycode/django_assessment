from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import CustomerSerializer, CustomerPaymentSerializer
from .models import Customer, CustomerPayment
from .services import create_customer_payments


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

    customer.is_valid(raise_exception=True)
    customer.save()
    create_customer_payments(customer.data['id'])
    return Response(
        status=status.HTTP_201_CREATED,
        data=customer.data,
    )


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
    data.is_valid(raise_exception=True)
    data.save()
    return Response(data.data)


@api_view(['DELETE'])
def delete_customer(request, pk):
    """Endpoint for delete customer"""
    customer = get_object_or_404(Customer, pk=pk)
    customer.delete()
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def view_customer_payments(request, pk):
    """Endpoint for list all customer payments"""
    customer = get_object_or_404(Customer, pk=pk)
    payments = CustomerPayment.objects.filter(customer_id=customer.id)

    if payments.exists():
        serializer = CustomerPaymentSerializer(payments, many=True)
        return Response(serializer.data)
    return Response(
        status=status.HTTP_204_NO_CONTENT,
        data=[],
    )
