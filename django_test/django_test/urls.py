"""django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webApp.views import *
urlpatterns = [
    path("generate_jwt/", generate_jwt, name='generate_jwt'),
    path("admin/", admin.site.urls),
    path("login/", login, name='login'),
    path("login_response/", login_response, name='login_response'),
    path("menu/", menu, name='menu'),
    path("logouts/", logouts, name='logouts'),
    path("create_customer/", create_customer, name='create_customer'),
    path("eliminar_customer/", eliminar_customer, name='eliminar_customer'),
    path("consulta_editar/", consulta_editar, name='consulta_editar'),
    path("editar_customer/", editar_customer, name='editar_customer'),
    path("list_customer/", list_customer, name='list_customer'),
    path("list_payments_customer/", list_payments_customer, name='list_payments_customer'),
    path("create_customer_api/", create_customer_api, name='create_customer_api'),
    path("update_customer_api/", update_customer_api, name='update_customer_api'),
    path("delete_customer_api/", delete_customer_api, name='delete_customer_api')






]
