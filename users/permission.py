from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrIsSelf(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj == request.user
