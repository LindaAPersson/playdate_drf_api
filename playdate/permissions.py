from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission class to allow only the owner of a playdate to edit or delete it.

    Methods:
        has_object_permission: Checks if the user has permission to perform the given action on the object.

    Attributes:
        request (Request): The incoming request.
        view (APIView): The view associated with the request.
        obj (Playdate): The playdate object being accessed.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.organizer == request.user
