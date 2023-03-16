 # -*- coding: utf-8 -*-

from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from webApp.views import CustomersViewSet, PaymentCustomersViewSet
from webApp.views import main, delete_customer, show_payments,update_customer,create_customer

router = DefaultRouter()
router.register(r'customers', CustomersViewSet, 'customer')
router.register(r'paymentcustomers', PaymentCustomersViewSet, 'paymentcustomer')

    
urlpatterns = [
    path(r'', include(router.urls)),
    path('main/', main, name='main'),
    path('delete/customer/<int:id>/', delete_customer, name='delete_customer'),
    path('show/payments/<int:id>/', show_payments, name='show_payments'),
    path('update/customer/<int:id>/', update_customer, name='update_customer'),
    path('create/customer/', create_customer, name='create_customer'),
]