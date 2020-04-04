import swapper
from rest_framework import serializers
import datetime

from bhawan_app.models import ComplaintTimeSlot
from bhawan_app.serializers.timing import TimingSerializer

class ComplaintTimeSlotSerializer(serializers.ModelSerializer):
    """
    Serializer for complaint time slot objects
    """

    timing = TimingSerializer(many=True)
    end = datetime.time(18,0,0)

    class Meta:
        """
        Meta class for ComplaintTimeSlotSerializer
        """

        model = ComplaintTimeSlot
        fields = [
            'complaint_type',
            'timing',
        ]

    def create(self, validated_data):
        # TODO: Set the end time to `self.end` if end is none
        pass
