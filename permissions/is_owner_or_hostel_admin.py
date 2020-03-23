from rest_framework import permissions

from formula_one.enums.active_status import ActiveStatus

from bhawan_app.managers.get_hostel_admin import get_hostel_admin


class IsOwnerOrHostelAdmin(permissions.BasePermission):
    """
    Object-level permission to only allow owners and admin of an object to edit
    it.
    """

    def is_hostel_admin(self, person):
        """
        Returns if the person is hostel admin or not
        :param person: an instance of the Person model whose roles are sought
        :return: if the person is hostel admin or not
        """

        hostel_admin = get_hostel_admin(person, ActiveStatus.IS_ACTIVE)
        return hostel_admin is not None

    def has_object_permission(self, request, view, obj):
        """
        Returns if the authenticated user has the permissions to access a
        particular object
        :param obj: an instance of the bhawan app models whose permissions is
        checked
        :return: if the the person is allowed or not
        """

        return obj.person == request.user.person or self.is_hostel_admin(
            request.user.person
        )
