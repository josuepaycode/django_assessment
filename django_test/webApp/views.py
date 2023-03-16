from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from webApp.models import Customer, PaymentCustomer
from webApp.serializers import CustomerSerializer, PaymentCustomerSerializer
from rest_framework import permissions, viewsets
from webApp.permission import hasPermissions
import random


@login_required(login_url='/users/login')
def main(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        return render(request, 'main.html', {'customers': customers, 'is_superadmin': bool(request.user.rol=='super_administrador')})

@login_required(login_url='/users/login')
def delete_customer(request, id):
    if request.user.rol!='super_administrador':
        raise Exception("Don't have the permissions")
    Customer.objects.get(id=id).delete()
    return redirect('main')

@login_required(login_url='/users/login')
def show_payments(request, id):
    customer = Customer.objects.get(id=id)
    payments = PaymentCustomer.objects.filter(customer=customer)
    return render(request, 'main.html', {"payments":payments, 'is_superadmin': bool(request.user.rol=='super_administrador')})

@login_required(login_url='/users/login')
def update_customer(request, id):
    if request.user.rol!='super_administrador':
        raise Exception("Don't have the permissions")
    if request.method == 'GET':
        customer = Customer.objects.get(id=id)
        return render(request, 'main.html', {'customer': customer, 'is_superadmin': bool(request.user.rol=='super_administrador')})
    if request.method =='POST':
        customer = Customer.objects.filter(id=id)
        customer.update(name=request.POST.get('name'), paternal_surname=request.POST.get('paternal_surname'), email=request.POST.get('email'))
        return redirect('main')

@login_required(login_url='/users/login')
def create_customer(request):
    if request.user.rol!='super_administrador':
        raise Exception("Don't have the permissions")
    if request.method =='POST':
        customer = Customer.objects.create(name=request.POST.get('name'), paternal_surname=request.POST.get('paternal_surname'), email=request.POST.get('email'))
        for n in range(random.randint(1,10)):
            PaymentCustomer.objects.create(customer=customer, amount=random.randint(1, 10000), quantity=random.randint(1,100), product_name=f"product {random.randint(1,1000)}")
        return redirect('main')


# REST Services


class CustomersViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, hasPermissions)
    serializer_class = CustomerSerializer

    def get_queryset(self):
        customers = Customer.objects.all()
        return customers
    
class PaymentCustomersViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PaymentCustomerSerializer
    permission_classes = (permissions.IsAuthenticated, hasPermissions)

    def get_queryset(self):
        payments = PaymentCustomer.objects.all()
        return payments
    
