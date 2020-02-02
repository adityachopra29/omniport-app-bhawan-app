from rest_framework import serializers
from bhawan_app.models import Facility


class FacilitySerializer(serializers.ModelSerializer):
    """
    Serializer for Facility objects
    """

    class Meta:
        """
        Meta class for FacilitySerializer
        """

        model = Facility
        fields = [
            'name',
            'description',
            'display_picture'
        ]
