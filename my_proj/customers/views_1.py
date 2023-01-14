from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from customers.models import Customer, Payment_Customer

class CustomerList(ListView):
    model = Customer

class CustomerView(DetailView):
    model = Customer

class CustomerCreate(CreateView):
    model = Customer
    fields = ['name', 'paternal_surname','email']
    success_url = reverse_lazy('customer_list')

class CustomerUpdate(UpdateView):
    model = Customer
    fields = ['name', 'paternal_surname','email']
    success_url = reverse_lazy('customer_list')

class CustomerDelete(DeleteView):
    model = Customer
    success_url = reverse_lazy('customer_list')


class Payment_Customer_List(ListView):
    model = Payment_Customer
    template_name = 'payment_customer_list'
    context_object_name = 'customer'

    def get_queryset(self):
        qs = Payment_Customer.objects.filter(customer_id=self.kwargs.get('customer_id'))
        return qs
