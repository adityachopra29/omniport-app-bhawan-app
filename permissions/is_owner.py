from rest_framework import permissions
from bhawan_app.managers.services import is_hostel_admin


class IsOwner(permissions.BasePermission):
    """
    Object-level permission to only allow owners and admin of an object to edit
    it.
    """

    def has_object_permission(self, request, view, obj):
        """
        Returns if the authenticated user has the permissions to access a
        particular object
        :param obj: an instance of the bhawan app models whose permissions is
        checked
        :return: if the the person is allowed or not
        """
    
        return obj == request.person