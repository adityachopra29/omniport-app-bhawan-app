import swapper

from rest_framework import serializers

from kernel.managers.get_role import get_role
from formula_one.mixins.period_mixin import ActiveStatus

from bhawan_app.managers.get_hostel_admin import get_hostel_admin

ResidentialInformation = swapper.load_model('Kernel', 'ResidentialInformation')


class PersonalInfoSerializer(serializers.ModelSerializer):
    """
    Serializer for ResidentialInformation objects
    """

    residence = serializers.CharField(
        source='residence.code',
    )
    is_admin = serializers.SerializerMethodField(
        read_only=True,
    )
    full_name = serializers.CharField(
        source='person.full_name',
    )
    id = serializers.SerializerMethodField()

    class Meta:
        """
        Meta class for PersonalInfoSerializer
        """

        model = ResidentialInformation
        fields = [
            'id',
            'is_admin',
            'full_name',
            'residence',
            'room_number',
        ]

    def get_id(self, obj):
        """
        Returns a unique identification ID for the logged in person
        :param obj: an instance of ResidentialInformation
        :return: a unique identification ID for the logged in person
        """

        role_student = get_role(
            person=obj.person,
            role_name='Student',
            active_status=ActiveStatus.IS_ACTIVE,
            silent=True,
        )
        role_faculty_member = get_role(
            person=obj.person,
            role_name='FacultyMember',
            active_status=ActiveStatus.IS_ACTIVE,
            silent=True,
        )
        if role_student is not None:
            return obj.person.student.enrolment_number
        elif role_faculty_member is not None:
            return obj.person.faculty_member.employee_id
        else:
            return obj.person.id

    def get_is_admin(self, obj):
        """
        Checks if the authenticated user is a hostel administrator or not
        :param obj: an instance of ResidentialInformation
        :return: a boolean if the authenticated user is a hostel administrator
        or not
        """

        if get_hostel_admin(obj.person) is None:
            return False
        return True
