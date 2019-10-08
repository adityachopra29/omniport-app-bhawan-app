from rest_framework import serializers
from bhawan_app.models import HostelFacility


class HostelFacilitySerializer(serializers.ModelSerializer):
    """
    Serializer for HostelFacility objects
    """

    class Meta:
        """
        Meta class for HostelFacilitySerializer
        """

        model = HostelFacility
        fields = [
            'name',
            'description',
            'display_picture'
        ]
