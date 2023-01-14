from django.urls import path

from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('customers', views.customer_list, name='customer_list'),
   path('view/<int:pk>', views.customer_view, name='customer_view'),
   path('new', views.customer_create, name='customer_new'),
   path('edit/<int:pk>', views.customer_update, name='customer_edit'),
   path('delete/<int:pk>', views.customer_delete, name='customer_delete'),
   path('payment_customer/<int:pk>/detail/', views.payment_customer_list, name='payment_customer_list'),
   

]
