from django.urls import path
from authentication import views

urlpatterns = [
    path('register', views.create_auth_admin, name="create-admin"),
    path('login', views.login, name="login"),
]
