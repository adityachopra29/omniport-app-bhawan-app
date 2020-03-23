from rest_framework import serializers

from formula_one.serializers.generics.contact_information import (
    ContactInformationSerializer,
)
from bhawan_app.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    """
    Serializer for Contact objects
    """

    person = serializers.CharField(source="person.full_name",)
    contact_information = ContactInformationSerializer(
        source="person.contact_information", many=True,
    )
    display_picture = serializers.ImageField(source="person.display_picture",)

    class Meta:
        """
        Meta class for ContactSerializer
        """

        model = Contact
        fields = [
            "id",
            "person",
            "designation_name",
            "contact_information",
            "display_picture",
        ]
