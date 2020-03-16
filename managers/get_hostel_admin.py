from formula_one.enums.active_status import ActiveStatus

from bhawan_app.models.roles import HostelAdmin


def get_hostel_admin(person, active_status=ActiveStatus.ANY):
    """
    Determines if the person has hostel administrator privileges
    :param person: an instance of the Person model whose roles are sought
    :param active_status: whether the role was, is, isn't or will be active
    :return: the role, if the person fulfills it
    """

    try:
        queryset = HostelAdmin.objects_filter(active_status)
        role = HostelAdmin.objects.get(person=person)
        return role
    except HostelAdmin.DoesNotExist:
        return None
