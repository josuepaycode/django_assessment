from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from .models import Administrator


class CustomUserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email']
    readonly_fields = ('date_joined','last_login')
    fieldsets = (
        (_("User Details"), {'fields': ('email', 'password', 'name', 'role')}),
        (_("Account Details"), {'fields': ('date_joined', 'last_login')}),
        (_("Permissions"), {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        ("User Details", {'fields': ('email', 'password1', 'password2')}),
    )


admin.site.register(Administrator, CustomUserAdmin)
admin.site.unregister(Group)
