from datetime import datetime, timedelta, timezone
import random
import jwt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import status
from .models import Customer, PaymentCustomer, Administrator
from .forms import LoginForm, CustomerForm
from .serializers import CustomerSerializer, PaymentCustomerSerializer


class CustomerListView(ListView):
    model = Customer
    template_name = "webApp/index.html"

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        return context
    

class CustomerCreateView(CreateView):
    form_class = CustomerForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(self.request.POST)
        if form.is_valid():
            customer = form.save()
            for i in range(random.randrange(1,4)):
                payment = PaymentCustomer(
                    amount = random.randrange(100,10000),
                    customer = customer,
                    product_name = random.choice(['shirts', 'jeans', 'shoes']),
                    quantity = random.randrange(1,50)
                )
                payment.save()
            messages.success(request, 'customer created successfully.')
            return JsonResponse({'valid':True}, status=200)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    
    
class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy('customer-list')
    
    
class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy('customer-list')


class Login(FormView):
    template_name = 'webApp/login.html'
    form_class = LoginForm

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        password = request.POST['password']
        form = self.get_form()
        if Administrator.objects.filter(name=name, password=password).exists():
            user = Administrator.objects.get(name=name)
            request.session['rol'] = user.rol
            return HttpResponseRedirect(reverse_lazy('customer-list'))
        messages.error(request, 'User no exists.')
        return self.form_invalid(form)
    
    
#APIS
#api para generar token al usuario
class LoginApiView(APIView):

    def post(self, request):
        name = request.data['name']
        password = request.data['password']
        if Administrator.objects.filter(name=name, password=password).exists():
            administrator = Administrator.objects.get(name=name, password=password)
            key = "secret" 
            payload = {
                'name':name,
                'password': password,
                'rol': administrator.rol,
                "exp": datetime.now(tz=timezone.utc) + timedelta(hours=8),
                }
            encode = jwt.encode(payload, key, algorithm="HS256")
            return Response({'Token': encode}, status=status.HTTP_201_CREATED)
        else:
            return Response({'Erro:': 'Ususario no encontrado'}, status=status.HTTP_404_NOT_FOUND)


#API para listar y crear customers    
class CustomerListApiView(APIView):

    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        token = request.headers['token']
        token_decode = jwt.decode(token, "secret", algorithms="HS256")
        if token_decode['rol'] == 'super_administrator':
            serializer = CustomerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Error":"No have permissions for create customer"}, status=status.HTTP_401_UNAUTHORIZED)
        

class CustomerDetail(APIView):

    def get_object(self,pk):
        return get_object_or_404(Customer, pk=pk)
    
    def get(self, request, pk):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    
    def put(self, request, pk):
        token = request.headers['token']
        token_decode = jwt.decode(token, "secret", algorithms="HS256")
        if token_decode['rol'] == 'super_administrator':
            customer = self.get_object(pk)
            serializer = CustomerSerializer(customer, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Error":"No have permissions for update customer"}, status=status.HTTP_401_UNAUTHORIZED)
        
    def delete(self, request, pk):
        token = request.headers['token']
        token_decode = jwt.decode(token, "secret", algorithm="HS256")
        if token_decode['rol'] == 'super_administrator':
            customer = self.get_object(pk)
            customer.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"Error":"No have permissions for delete customer"}, status=status.HTTP_401_UNAUTHORIZED)
        
    
class PaymentsCustomerListApiView(ListAPIView):
    queryset = PaymentCustomer.objects.all()
    serializer_class = PaymentCustomerSerializer


    






