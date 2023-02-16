from django.contrib import admin

from webApp.models import Administrators, Customers, Payments_Customers

# Register your models here.

admin.site.register(Administrators)
admin.site.register(Customers)
admin.site.register(Payments_Customers)