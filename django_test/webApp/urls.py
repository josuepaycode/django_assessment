from django.urls import path
from .views import *

urlpatterns = [
    path('customer/list/', CustomerListView.as_view(), name='customer-list'),
    path('customer/login/', Login.as_view(), name='login'),
    path('customer/create/', CustomerCreateView.as_view(), name='customer-create'),
    path('customer/edit/<int:pk>/', CustomerUpdateView.as_view(), name='customer-update'),
    path('customer/delete/<int:pk>/', CustomerDeleteView.as_view(), name='customer-delete'),
    path('api/login/', LoginApiView.as_view()),
    path('api/customers/', CustomerListApiView.as_view()),
    path('api/payments_customer/', PaymentsCustomerListApiView.as_view()),
    path('api/customers/<int:pk>/', CustomerDetail.as_view()),

]
