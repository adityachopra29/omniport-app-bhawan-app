from rest_framework import mixins, viewsets

from bhawan_app.models import HostelRoomBooking
from bhawan_app.serializers.hostel_room_booking import HostelRoomBookingSerializer


class HostelRoomBookingViewset(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    """
    Detail view for getting contact information of a single hostel
    """

    serializer_class = HostelRoomBookingSerializer
    queryset = HostelRoomBooking.objects.all() 

