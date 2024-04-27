from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission class to allow only the owner of an object to edit it.

    Attributes:
        request: The HTTP request object.
        view: The API view object.
        obj: The object being accessed.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
