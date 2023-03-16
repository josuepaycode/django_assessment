from django.contrib import admin


from users.models import Administrators

class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(Administrators, UserAdmin)