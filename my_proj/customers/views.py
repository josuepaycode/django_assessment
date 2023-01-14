from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from customers.models import Customer, Payment_Customer
import random
from .fake_data import  create_payment
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'customers/home.html', {})




class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'paternal_surname','email']

def customer_list(request, template_name='customers/customer_list.html'):
    customer = Customer.objects.all()
    data = {}
    data['customers_list'] = customer
    return render(request, template_name, data)

def payment_customer_list(request,pk, template_name='customers/payment_customer_list.html'):
    payment_customer = Payment_Customer.objects.filter(customer_id=pk)
    print(payment_customer)
    data = {}
    data['payment_customer_list'] = payment_customer
    return render(request, template_name, data)

def customer_view(request, pk, template_name='customers/customer_detail.html'):
    customer= get_object_or_404(Customer, pk=pk)
    email = customer.email
    surname = customer.paternal_surname
    print(type(customer))    
    return render(request, template_name, {'customer':customer,'surname':customer.paternal_surname})

def customer_create(request, template_name='customers/customer_form.html'):
    form = CustomerForm(request.POST or None)
    #
    if form.is_valid():
        print(form)
        form.save()
        payment_customer_create(form.instance.id)
        return redirect('customer_list')
    return render(request, template_name, {'form':form})


def payment_customer_create(customer_id):
    #amount,quantity,customer_id,product_name
    random_create = random.randint(1,10)
    for i in range(random_create):
        product_name,quantity,amount=create_payment()
        customer = Customer.objects.filter(pk=customer_id).first()
        payment_customer = Payment_Customer(customer_id=customer,amount=amount,product_name=product_name,quantity=quantity)
        print(payment_customer)
        payment_customer.save()




def customer_update(request, pk, template_name='customers/customer_form.html'):
    customer= get_object_or_404(Customer, pk=pk)
    form = CustomerForm(request.POST or None, instance=customer)
    if form.is_valid():
        form.save()
        return redirect('customer_list')
    return render(request, template_name, {'form':form})

def customer_delete(request, pk, template_name='customers/customer_confirm_delete.html'):
    customer= get_object_or_404(Customer, pk=pk)    
    if request.method=='POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, template_name, {'object':customer})