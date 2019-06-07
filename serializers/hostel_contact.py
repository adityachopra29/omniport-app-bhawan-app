from rest_framework import serializers

from formula_one.serializers.generics.contact_information import (
    ContactInformationSerializer,
)
from bhawan_app.models import HostelContact


class HostelContactSerializer(serializers.ModelSerializer):
    """
    Serializer for HostelContact objects
    """

    person = serializers.CharField(
        source='person.full_name',
    )
    contact_information = ContactInformationSerializer(
        source='person.contact_information',
        many=True,
    )
    display_picture = serializers.ImageField(
        source='person.display_picture',
    )

    class Meta:
        """
        Meta class for HostelContactSerializer
        """

        model = HostelContact
        fields = [
            'person',
            'designation_name',
            'contact_information',
            'display_picture',
        ]
