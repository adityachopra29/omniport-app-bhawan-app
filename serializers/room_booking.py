import swapper

from rest_framework import serializers

from bhawan_app.models import RoomBooking
from bhawan_app.serializers.relative import RelativeSerializer

Hostel = swapper.load_model('Kernel', 'Residence')

class RoomBookingSerializer(serializers.ModelSerializer):
    """
    Serializer for RoomBooking objects
    """

    booked_by = serializers.CharField(
        source='person.full_name',
        read_only=True,
    )
    relative = RelativeSerializer(
        many=True,
    )

    class Meta:
        model = RoomBooking
        fields = [
            'id',
            'booked_by',
            'status',
            'requested_from',
            'requested_till',
            'booked_by_room_no',
            'relative',
        ]
        # extra_kwargs = {
        #   'booked_by_room_no':{'read_only': True} But no available in db
        # }

    def create(self, validated_data):
        """
        Get relative field
        """
        relatives = validated_data.pop('relative')
        relatives_serializer = RelativeSerializer(data=relatives, many=True)

        """
        Get hostel, hostel__code from request url using context from views
        """
        hostel_code = self.context['hostel__code']
        hostel = Hostel.objects.get(code=hostel_code)
        relatives_serializer.is_valid(raise_exception=True)

        """
        Get authenticated user and make a RoomBooking instance
        """
        person = self.context['person']
        room_booking = RoomBooking.objects.create(
            **validated_data,
            hostel=hostel,
            person=person,
        )

        """
        Populate the relatives with current booking and authenticated user
        """
        for relative in relatives_serializer.validated_data:
            relative['booking'] = room_booking

        relatives_serializer.save()

        return room_booking