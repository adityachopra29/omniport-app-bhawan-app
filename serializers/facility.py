import swapper

from rest_framework import serializers
from bhawan_app.models import Facility, Timing
from bhawan_app.serializers.timing import TimingSerializer

Hostel = swapper.load_model('Kernel', 'Residence')

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

    def create(self, validated_data):
        timing_data = validated_data.pop('timings')
        timing_serializer = TimingSerializer(data=timing_data, many=True)
        timing_serializer.is_valid(raise_exception=True)

        hostel_code = self.context['hostel__code']
        hostel = Hostel.objects.get(code=hostel_code) #TO be seen
        timing_objects = timing_serializer.save()
        name = self.context['name']
        facility = Facility.objects.create(
            **validated_data,
            hostel=hostel,
            name=name,
        )

        for timing in timing_objects:
            facility.timings.add(timing)

        return facility

    