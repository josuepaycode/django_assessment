from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name='home'),
    path('customer/<int:pk>/delete', views.delete_customer, name='delete-customer'),
    path('customer/<int:pk>/update', views.update_customer, name='update-customer'),
    path('customer/create', views.add_customer, name='add-customer'),
    path('customer', views.view_customers, name='view-customers'),
]
