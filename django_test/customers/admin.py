from django.contrib import admin

from customers.models import Customer

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = (
        "name",
        "paternal_surname",
        "email",
        "id",
    )
