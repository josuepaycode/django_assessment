from django.urls import path
from . import views

urlpatterns=[
  path('',views.home,name='home'),
  path('clientes/',views.clientes,name='clientes'),
  path('nuevocliente/',views.nuevocliente,name='nuevocliente'),
  path('clientes/editcustomer/<int:id>',views.editcustomer,name='editcustomer'),
  path('clientes/eliminarcustomer/<int:id>',views.eliminarcustomer,name='eliminarcustomer'),
  path('clientes/editcustomer/changecustomer/',views.changecustomer,name='changecustomer')
]