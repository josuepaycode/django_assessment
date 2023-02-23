from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from .models import Customers, PaymentsCustomers, Administrators
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
import datetime
import base64



# Create your views here.
""" CRUD """
@login_required(login_url='/app/login')
def index(request):
    customers = Customers.objects.all()
    payments = PaymentsCustomers.objects.all()
    rol = request.session['rol']
    return render(request,'index/index.html',{'customers':customers, 'payments':payments, 'rol' : rol})

def login_page(request):
	return render(request,'login/login.html')

def login_user(request):
    if request.method == 'POST':
        name = request.POST.get('user', '')
        password = request.POST.get('password', '')
        user = authenticate(username=name, password=password)
        
        if user is not None and user.is_active:
            
            admin = Administrators.objects.get(name=name,password=password)
            if admin:
                request.session['rol'] = admin.rol

            login(request, user)
            return redirect('/app')
        
        else:
            return render(request,'login/login.html',{'error': True, 'message': 'Nombre de usuario o contraseña incorrecta.'})

@login_required(login_url='/app/login')
def logout_user(request):
    logout(request)
    return redirect('/app/login')

@login_required(login_url='/app/login')
def get_customer(request,id):
    customer = Customers.objects.get(id=id)
    data = dict()
    data['id'] = customer.id
    data['name'] = customer.name
    data['surname'] = customer.paternal_surname
    data['email'] = customer.email
    return JsonResponse(data)

@login_required(login_url='/app/login')
def save_customer(request):
    id = request.POST.get('id','')
    name = request.POST.get('name','')
    paternal_surname = request.POST.get('paternal_surname','')
    email = request.POST.get('email','')

    customer = Customers.objects.get(id=id)
    customer.name = name
    customer.paternal_surname = paternal_surname
    customer.email = email
    customer.updated_at = datetime.datetime.now()
    customer.save()
    return redirect('/app')

@login_required(login_url='/app/login')
def delete_customer(request):
    id = request.POST.get('deleteid','')
    
    customer = Customers.objects.get(id=id)
    customer.delete()
    return redirect('/app')

@login_required(login_url='/app/login')
def create_customer(request):
    name = request.POST.get('name','')
    paternal_surname = request.POST.get('paternal_surname','')
    email = request.POST.get('email','')
    customer = Customers(name=name,paternal_surname=paternal_surname,email=email)
    customer.save()
    return redirect('/app')



""" REST API """

def rest_api_auth(function):

    def wrapper(*args, **kwargs):

        basic_token = str(args[1].META['HTTP_AUTHORIZATION']).split('Basic ')[1]
        basic_token = base64.b64decode(basic_token)
        credentials = basic_token.decode('UTF-8')
        credentials = str(credentials).split(':')

        admins = Administrators.objects.filter(name=credentials[0],password=credentials[1])
        data = dict()
        method = args[1].method

        print(type(args[1].method))
        if len(admins) > 0:
            admin = Administrators.objects.get(name=credentials[0],password=credentials[1])
           
            if method != "GET":
                
                if admin.rol == 'S':
                    return function(*args, **kwargs)
                
                else:
                    data["message"] = "Not Authenticated"        
                    return JsonResponse(data)
            
            return function(*args,**kwargs)
        
        else:
            data["message"] = "Not Authenticated"
            return JsonResponse(data)
    
    return wrapper

class CustomerView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    @rest_api_auth
    def get(self, request, id=0):
        
        if id > 0:
            customers = list(Customers.objects.filter(id=id).values())
            
            if len(customers)>0:
                customers = customers[0]
        
        else:    
            customers = list(Customers.objects.values())
        
        if len(customers) > 0:
            data = {"message":"success", "data":customers} 
        
        else:
            data = {"message":"no customers", "data":[]}
        
        return JsonResponse(data)
    
    @rest_api_auth
    def post(self,request):
        """ Solo super administrador """
        json_data = json.loads(request.body)
        customer = Customers(name=json_data['name'],paternal_surname=json_data['paternal_surname'],email=json_data['email'])
        customer.save()
        if customer:
            data = {"message":"success", "id":customer.id}
            return JsonResponse(data)
        else:
            data = {"message":"error while creating"}
            return JsonResponse(data)

    @rest_api_auth
    def put(self, request, id):
        """ Solo super administrador """
        json_data = json.loads(request.body)
        customers = Customers.objects.filter(id=id)
        if len(customers) > 0:
            customer = Customers.objects.get(id=id)
            customer.name = json_data['name']
            customer.paternal_surname = json_data['paternal_surname']
            customer.email = json_data['email']
            customer.updated_at = datetime.datetime.now()
            customer.save()

            data = {"message":"success"}

            return JsonResponse(data)
        else:
            data = {"message" : "customer not found"}
            return JsonResponse(data)

    @rest_api_auth
    def delete(self, request, id):
        """ Solo super administrador """
        json_data = json.loads(request.body)
        
        customers = Customers.objects.filter(id=id)
        
        if len(customers) > 0:
            customer = Customers.objects.get(id=id)
            customer.delete()

            data = {"message" : "success"}
            return JsonResponse(data)
        else:
            data = {"message" : "customer not found"}
            return JsonResponse(date)

class PaymentView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

   
    #Se pasa el id del cliente
    @rest_api_auth
    def get(self, request, id=0):
        
        if id > 0:
            customers = Customers.objects.filter(id=id)
            if len(customers) > 0:
                customer = Customers.objects.get(id=id)
                payments = list(PaymentsCustomers.objects.filter(customer=customer).values())
        else:    
            payments = list(PaymentsCustomers.objects.values())
        
        if len(payments) > 0:
            data = {"message":"success", "data":payments} 
        
        else:
            data = {"message":"no payments", "data":[]}
        
        return JsonResponse(data)
    def post(self, request):
        pass
    def put(self, request):
        pass
    def delete(self, request):
        pass

