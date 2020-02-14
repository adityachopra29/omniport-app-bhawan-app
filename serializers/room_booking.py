import swapper

from rest_framework import serializers

from bhawan_app.models import RoomBooking
from bhawan_app.serializers.visitor import VisitorSerializer

Hostel = swapper.load_model('kernel', 'Residence')


class RoomBookingSerializer(serializers.ModelSerializer):
    """
    Serializer for RoomBooking objects
    """

    booked_by = serializers.CharField(
        source='person.full_name',
        read_only=True,
    )
    visitor = VisitorSerializer(
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
            'visitor',
        ]

    def create(self, validated_data):
        """
        Get visitor field
        """
        visitors = validated_data.pop('visitor')
        visitors_serializer = VisitorSerializer(data=visitors, many=True)

        """
        Get hostel, hostel__code from request url using context from views
        """
        hostel_code = self.context['hostel__code']
        hostel = Hostel.objects.get(code=hostel_code)
        visitors_serializer.is_valid(raise_exception=True)

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
        Populate the Visitors with current booking and authenticated user
        """
        for visitor in visitors_serializer.validated_data:
            visitor['booking'] = room_booking

        visitors_serializer.save()

        return room_booking
