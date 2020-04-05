import swapper
from rest_framework import serializers
import datetime

from bhawan_app.models import ComplaintTimeSlot
from bhawan_app.serializers.timing import TimingSerializer

Hostel = swapper.load_model("Kernel", "Residence")

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
            'id',
        ]

    def create(self, validated_data):
        """
        Get timing field and serialize it.
        """
        timings = validated_data.pop('timing')
        timings_serializer = TimingSerializer(data=timings, many=True)
        timings_serializer.is_valid(raise_exception=True)

        """
        Get hostel from context and make a ComplaintSlot instance
        """
        hostel_code = self.context["hostel__code"]
        hostel = Hostel.objects.get(code=hostel_code)
        time_slot = ComplaintTimeSlot.objects.create(
            **validated_data, hostel=hostel,
        )

        """
        Populate the 'timings' of a time_slot.
        """
        timing_objects = timings_serializer.save()
        time_slot.timing.add(*timing_objects)

        return time_slot

    def update(self, instance, validated_data):
        """
        Get timing field and serialize it.
        """
        timings = validated_data.pop('timing')
        timings_serializer = TimingSerializer(data=timings, many=True)
        timings_serializer.is_valid(raise_exception=True)
        timing_objects = timings_serializer.save()
        instance.timing.clear()
        instance.timing.add(*timing_objects)
        return instance