import swapper

from rest_framework import serializers

from bhawan_app.models import RoomBooking
from bhawan_app.serializers.relative import RelativeSerializer

class RoomBookingSerializer(serializers.ModelSerializer):
    """
    Serializer for RoomBooking objects
    """
    hostel = serializers.CharField(
        source='hostel.name',
        read_only=True,
    )
    hostel_code = serializers.CharField(
        source='hostel.code',
    )
    booked_by = serializers.CharField(
        source='person.full_name',
    )
    visitor = RelativeSerializer(
        source='relative',
        many=True,
    )

    class Meta:
        model = RoomBooking
        fields = [
            'id',
            'booked_by',
            'hostel',
            'status',
            'requested_from',
            'requested_till',
            'booked_by_room_no',
            'hostel_code',
            'visitor',
        ]

    def create(self, validated_data):
        Residence = swapper.load_model('Kernel', 'Residence')
        hostel_code = validated_data['hostel']['code']
        hostel = Residence.objects.get(code=hostel_code)
        validated_data['hostel'] = hostel
        return super().create(validated_data)
