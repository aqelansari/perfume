from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
   def has_permission(self, request, view):
      return request.user.is_superuser

class IsStaff(BasePermission):
   def has_permission(self, request, view):
      return request.user.is_staff

class IsActive(BasePermission):
   def has_permission(self, request, view):
      return request.user.is_active