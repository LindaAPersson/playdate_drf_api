from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permission class to check if the requesting user is the owner of the object.

    Attributes:
        request (Request): The request being made.
        view (View): The view associated with the request.
        obj (object): The object being accessed.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.organizer == request.user