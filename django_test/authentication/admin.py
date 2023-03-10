from django.contrib import admin
from .models import Administrator, UserAdmin


admin.site.register(Administrator, UserAdmin)
