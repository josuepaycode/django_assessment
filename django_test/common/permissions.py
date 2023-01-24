from rest_framework import permissions

class IsSuperAdminPermission(permissions.BasePermission):
    message = 'Adding customers not allowed.'

    def has_permission(self, request, view):
        if request.user and request.user.is_superuser:
            return True
        return False
