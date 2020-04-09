import swapper
from datetime import datetime

from rest_framework import serializers

from formula_one.models.generics.contact_information import ContactInformation
from bhawan_app.models import RoomBooking
from bhawan_app.serializers.visitor import VisitorSerializer


class RoomBookingSerializer(serializers.ModelSerializer):
    """
    Serializer for RoomBooking objects
    """

    booked_by = serializers.CharField(
        source='person.full_name',
        read_only=True,
    )
    booked_by_room_no = serializers.CharField(
        source='person.residentialinformation.room_number',
        read_only=True,
    )
    visitor = VisitorSerializer(
        many=True,
    )
    phone_number = serializers.SerializerMethodField()

    class Meta:
        model = RoomBooking
        fields = [
            'id',
            'booked_by',
            'status',
            'requested_from',
            'requested_till',
            'visitor',
            'booked_by_room_no',
            'phone_number',
            "datetime_modified"
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
        visitors_serializer.is_valid(raise_exception=True)

        """
        Get authenticated user and make a RoomBooking instance
        """
        person = self.context["person"]
        room_booking = RoomBooking.objects.create(
            **validated_data, person=person,
        )

        """
        Populate the Visitors with current booking and authenticated user
        """
        for visitor in visitors_serializer.validated_data:
            visitor['booking'] = room_booking

        visitors_serializer.save(datetime_modified=datetime.now())

        return room_booking

    def get_phone_number(self, obj):
        """
        Returns the primary phone number of the person who booked room
        :return: the primary phone number of the person who booked room
        """

        try:
            contact_information = \
                ContactInformation.objects.get(person=obj.person)
            return contact_information.primary_phone_number
        except ContactInformation.DoesNotExist:
            return None