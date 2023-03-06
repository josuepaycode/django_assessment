from django.contrib import admin

from webApp.models import administrators, customer, payments_customer


admin.site.register(administrators)
admin.site.register(customer)
admin.site.register(payments_customer)
