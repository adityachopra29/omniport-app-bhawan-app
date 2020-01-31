from rest_framework import permissions

class IsOwnerOrHostelAdmin(permissions.BasePermission):
    """
    Object-level permission to only allow owners and admin of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_permission(self, request, view):
        if view.action == 'list':
            print(view.action)
            return request.user.is_superuser
        return request.user.is_superuser or request.user.isAuthenticated
        
    def has_object_permission(self, request, view, concerned_user):
        return concerned_user == request.user or request.user.is_superuser