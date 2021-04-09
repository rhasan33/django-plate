from rest_framework.permissions import BasePermission


class IsSuperUser(BasePermission):
    def has_permission(self, request, view) -> bool:
        return request.user.is_superuser


class IsStaff(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff
