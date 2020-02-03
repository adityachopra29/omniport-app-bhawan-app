from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from bhawan_app.models import RoomBooking
from bhawan_app.permissions.is_owner_or_hostel_admin import (
    IsOwnerOrHostelAdmin,
)
from bhawan_app.serializers.room_booking import RoomBookingSerializer
from bhawan_app.managers.get_hostel_admin import get_hostel_admin


class RoomBookingViewset(viewsets.ModelViewSet):

    """
    Detail view for getting contact information of a single hostel
    """

    serializer_class = RoomBookingSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrHostelAdmin, ]

    def get_queryset(self):
        """
        Return the queryset of bookings grouped by a hostel
        :return: the queryset of bookings grouped by a hostel
        """

        queryset = RoomBooking.objects.filter(
            hostel__code=self.kwargs['hostel__code']
        )
        return queryset
    
    def list(self, request, hostel__code):
        """
        List all the bookings according to permissions
        """

        queryset = self.get_queryset()
        if get_hostel_admin(request.user.person) is None:
            bookings = queryset.filter(booked_by=request.user.person)
        else:
            bookings = queryset
        serializer = RoomBookingSerializer(bookings, many=True)
        return Response(serializer.data)

    def retrieve(self, request, hostel__code, pk):
        """
        Retrieve a single object of room bookings
        """

        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=pk)
        self.check_object_permissions(request, obj.booked_by)
        serializer = RoomBookingSerializer(obj)
        return Response(serializer.data)
