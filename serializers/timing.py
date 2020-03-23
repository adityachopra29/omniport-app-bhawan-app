from rest_framework import serializers

from bhawan_app.models import Timing


class TimingSerializer(serializers.ModelSerializer):
    """
    Serializer for Profile objects
    """

    class Meta:
        """
        Meta class for ProfileSerializer
        """

        model = Timing
        fields = [
            "day",
            "start",
            "end",
            "description",
        ]
