from django.contrib import admin
from .models import Customer, CustomerPayment, Administrator

# Register your models here.
admin.site.register(Customer)
admin.site.register(CustomerPayment)
admin.site.register(Administrator)
