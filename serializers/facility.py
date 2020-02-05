from rest_framework import serializers
from bhawan_app.models import Facility
from bhawan_app.serializers.timing import TimingSerializer


class FacilitySerializer(serializers.ModelSerializer):
    """
    Serializer for Facility objects
    """

    timings = TimingSerializer(
        many=True,
    )

    class Meta:
        """
        Meta class for FacilitySerializer
        """

        model = Facility
        fields = [
            'id',
            'name',
            'description',
            'display_picture',
            'timings',
        ]
