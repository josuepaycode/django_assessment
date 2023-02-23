from . import views
from .views import CustomerView, PaymentView
from django.urls import path,re_path

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_page, name='login_page'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('customer/get/<int:id>',(views.get_customer), name='get_customer'),
    path('customer/put',views.save_customer,name="save_customer"),
    path('customer/post',views.create_customer,name="create_customer"),
    path('customer/delete',views.delete_customer,name="delete_customer"),

    #API REST
    path('customers/',CustomerView.as_view(), name="customers_list"),
    path('customers/<int:id>',CustomerView.as_view(), name="customers"),
    path('payments/',PaymentView.as_view(), name="payment_list"),
    path('payments/<int:id>',PaymentView.as_view(), name="payments")#Se pasa el id del cliente
]

