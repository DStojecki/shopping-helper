from rest_framework.permissions import BasePermission


class OwnerOnly(BasePermission):
    """
    Grant permissions only to the owner of the object
    """
    def has_object_permission(self, request, view, obj):
        return obj.created_by == request.user
