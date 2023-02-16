from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('dashboard/<int:id>',views.dashboard, name="dashboard")
]