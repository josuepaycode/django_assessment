from django.contrib import admin

# Register your models here.
from django.contrib import admin
from customers.models import Customer
from .models import User
admin.site.register(Customer)
admin.site.register(User)
