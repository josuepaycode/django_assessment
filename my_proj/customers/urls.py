from django.urls import path

from . import views

urlpatterns = [
    path('', views.CustomerList.as_view(), name='customer_list'),
    path('view/<int:pk>', views.CustomerView.as_view(), name='customer_view'),
    path('new', views.CustomerCreate.as_view(), name='customer_new'),
    path('view/<int:pk>', views.CustomerView.as_view(), name='customer_view'),
    path('edit/<int:pk>', views.CustomerUpdate.as_view(), name='customer_edit'),
    path('delete/<int:pk>', views.CustomerDelete.as_view(), name='customer_delete'),
]
