from rest_framework import permissions

class IsOwnerOrShared(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user in obj.shared_with.all()
