from rest_framework import mixins, viewsets
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

from bhawan_app.models import RoomBooking
from bhawan_app.permissions.is_owner_or_admin import IsOwnerOrHostelAdmin
from bhawan_app.serializers.room_booking import RoomBookingSerializer


class RoomBookingViewset(mixins.ListModelMixin,
                               mixins.CreateModelMixin,
                               mixins.RetrieveModelMixin,
                               viewsets.GenericViewSet):

    """
    Detail view for getting contact information of a single hostel
    """

    serializer_class = RoomBookingSerializer
    permission_classes = [IsOwnerOrHostelAdmin]

    def get_queryset(self):
        queryset = RoomBooking.objects.filter(hostel__code=self.kwargs['hostel__code'])
        return queryset

    def retrieve(self, request, hostel__code, pk):
        queryset = self.get_queryset()
        try:
            booking = queryset.get(pk=pk)
            self.check_object_permissions(request, booking.booked_by)
        except ObjectDoesNotExist:
            booking = None
        serializer = RoomBookingSerializer(booking)
        return Response(serializer.data)