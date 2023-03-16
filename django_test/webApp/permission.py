from rest_framework import permissions

class hasPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        success = True
        is_super_admin = request.user.rol == 'super_administrador'
        if not is_super_admin and request.method not in ('GET', 'HEAD', 'OPTIONS'):
            success = False 
        return success
    

    