from django.urls import path
from . import views

urlpatterns=[
    path('payments/',views.paymentsview,name='payments'),
    path('newpayment/',views.newpayment,name='newpayment')
]