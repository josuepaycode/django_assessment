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

    def has_add_permission(self, request, obj=None):
        if request.user and request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if request.user and request.user.is_superuser:
            return True
        return False
    
    def has_delete_permission(self, request, obj=None):
        if request.user and request.user.is_superuser:
            return True
        return False
