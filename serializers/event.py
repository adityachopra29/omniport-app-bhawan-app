from rest_framework import serializers
from bhawan_app.models import Event
from bhawan_app.serializers.timing import TimingSerializer


class EventSerializer(serializers.ModelSerializer):
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

        model = Event
        fields = [
            'id',
            'name',
            'date',
            'description',
            'display_picture',
            'timings',
        ]
