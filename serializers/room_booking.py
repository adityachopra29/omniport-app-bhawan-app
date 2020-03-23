import swapper

from rest_framework import serializers

from bhawan_app.models import RoomBooking
from bhawan_app.serializers.visitor import VisitorSerializer

Hostel = swapper.load_model('kernel', 'Residence')

<<<<<<< HEAD
=======
Hostel = swapper.load_model("Kernel", "Residence")

>>>>>>> Linting changes.

class RoomBookingSerializer(serializers.ModelSerializer):
    """
    Serializer for RoomBooking objects
    """

<<<<<<< HEAD
    booked_by = serializers.CharField(
        source='person.full_name',
        read_only=True,
    )
    visitor = VisitorSerializer(
        many=True,
    )
=======
    booked_by = serializers.CharField(source="person.full_name", read_only=True,)
    relative = RelativeSerializer(many=True,)
>>>>>>> Linting changes.

    class Meta:
        model = RoomBooking
        fields = [
<<<<<<< HEAD
            'id',
            'booked_by',
            'status',
            'requested_from',
            'requested_till',
            'visitor',
=======
            "id",
            "booked_by",
            "status",
            "requested_from",
            "requested_till",
            "booked_by_room_no",
            "relative",
>>>>>>> Linting changes.
        ]

    def create(self, validated_data):
        """
        Get visitor field
        """
<<<<<<< HEAD
        visitors = validated_data.pop('visitor')
        visitors_serializer = VisitorSerializer(data=visitors, many=True)
=======
        relatives = validated_data.pop("relative")
        relatives_serializer = RelativeSerializer(data=relatives, many=True)
>>>>>>> Linting changes.

        """
        Get hostel, hostel__code from request url using context from views
        """
        hostel_code = self.context["hostel__code"]
        hostel = Hostel.objects.get(code=hostel_code)
        visitors_serializer.is_valid(raise_exception=True)

        """
        Get authenticated user and make a RoomBooking instance
        """
        person = self.context["person"]
        room_booking = RoomBooking.objects.create(
            **validated_data, hostel=hostel, person=person,
        )

        """
        Populate the Visitors with current booking and authenticated user
        """
<<<<<<< HEAD
        for visitor in visitors_serializer.validated_data:
            visitor['booking'] = room_booking
=======
        for relative in relatives_serializer.validated_data:
            relative["booking"] = room_booking
>>>>>>> Linting changes.

        visitors_serializer.save()

        return room_booking
