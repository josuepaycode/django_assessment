from django.contrib import admin

# Register your models here.
from webApp.models import Customer, PaymentCustomer

class CustomerAdmin(admin.ModelAdmin):
    pass

class PaymentCustomerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Customer, CustomerAdmin)
admin.site.register(PaymentCustomer,PaymentCustomerAdmin)