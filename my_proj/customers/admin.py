from django.contrib import admin

# Register your models here.
from django.contrib import admin
from customers.models import Customer
from django.contrib.auth.models import Permission
from .models import User,Payment_Customer
admin.site.register(Customer)
admin.site.register(User)
admin.site.register(Payment_Customer)
admin.site.register(Permission)