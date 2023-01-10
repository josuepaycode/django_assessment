from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from .models import customers
from .forms import nuevoclienteform

from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
  page=loader.get_template('home.html')
  context={}
  return HttpResponse(page.render(context,request))

@login_required
def clientes(request):
  clients=customers.objects.all().values()   
  page=loader.get_template('customers/viewscustomers.html')
  context={'clients':clients}
  return HttpResponse(page.render(context,request))

@login_required
def nuevocliente(request):
  page=loader.get_template('customers/newcustomer.html')
  form=nuevoclienteform
  if request.method == 'POST':
    form=nuevoclienteform(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/newpayment')
    else:
      return redirect('/clientes')
  context={'form':form}
  return HttpResponse(page.render(context,request))

def editcustomer(request,id):
  page=loader.get_template('customers/editcustomer.html')
  customer_object=customers.objects.get(id_customer=id)
  context={'customer':customer_object}
  return HttpResponse(page.render(context,request))

def changecustomer(request):
  if request.method=='POST':
    id=request.POST['cus_id']
    nombre=request.POST['cus_nombre']
    apellido=request.POST['cus_apellido']
    correo=request.POST['cus_correo']

    customer = customers.objects.get(id_customer=id)
    customer.nombre_cliente=nombre
    customer.apellido_cliente=apellido
    customer.correo=correo
    customer.save()

  return redirect('/clientes')

def eliminarcustomer(request,id):
  customer_object=customers.objects.get(id_customer=id)
  customer_object.delete()

  return redirect('/')