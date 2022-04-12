from rest_framework.permissions import BasePermission

from src.accounts.utils import ADMIN, CLIENT_USER


class IsAdmin(BasePermission):
    """
    Allows access only to admin.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == ADMIN)


class IsAdminOrReadOnly(BasePermission):
    """
    Allows access only to admin.
    """

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return bool(request.user and request.user.is_authenticated and request.user.role == ADMIN)


class IsClientUser(BasePermission):
    """
    Allows access only to admin(CRUD) and operator(read only)
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == CLIENT_USER)
