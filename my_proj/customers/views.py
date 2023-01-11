from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from customers.models import Customer

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
