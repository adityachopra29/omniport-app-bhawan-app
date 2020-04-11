import swapper

from rest_framework import serializers

from bhawan_app.models.roles.hostel_admin import HostelAdmin
from formula_one.models.generics.contact_information import ContactInformation

Person = swapper.load_model('Kernel', 'Person')

class HostelAdminSerializer(serializers.ModelSerializer):
    """
    Serializer for Visitor objects
    """

    name = serializers.CharField(
        source='person.full_name',
        read_only=True,
    )
    email_address = serializers.SerializerMethodField()

    class Meta:
        """
        Meta class for ProfileSerializer
        """

        model = HostelAdmin
        fields = [
            'id',
            'designation',
            'name',
            'email_address',
        ]

    def get_email_address(self, admin):
        """
        Retrieves the email address for an Admin.
        """
        try:
            contact_information = \
                ContactInformation.objects.get(person=admin.person)
            return contact_information.email_address
        except ContactInformation.DoesNotExist:
            return None