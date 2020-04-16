from rest_framework import permissions


class IsSuperUser(permissions.BasePermission):
    # Permissão customizada para apenas Admin deletarem no model que essa Classe for chamada.
    def has_permission(self, request, view):
        if request.method == 'DELETE':
            if request.user.is_superuser:
                return True
            return False
        return True

