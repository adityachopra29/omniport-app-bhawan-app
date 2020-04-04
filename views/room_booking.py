from django.shortcuts import get_object_or_404

from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from bhawan_app.models import RoomBooking
from bhawan_app.serializers.room_booking import RoomBookingSerializer
from bhawan_app.managers.services import get_hostel_admin, is_supervisor, is_warden
from bhawan_app.constants import statuses


class RoomBookingViewset(viewsets.ModelViewSet):

    """
    Detail view for getting contact information of a single hostel
    """

    serializer_class = RoomBookingSerializer
    allowed_methods = ['GET', 'PATCH', 'POST']
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Return the queryset of bookings grouped by a hostel
        :return: the queryset of bookings grouped by a hostel
        """

        filters = {}
        filters['person__residentialinformation__residence__code'] = \
            self.kwargs['hostel__code']
        queryset = RoomBooking.objects.filter(**filters)
        return queryset

    def get_serializer_context(self):
        return {
            "person": self.request.person,
        }

    def list(self, request, hostel__code):
        """
        List all the bookings according to permissions
        """

        queryset = self.get_queryset()
        if get_hostel_admin(request.person) is None:
            bookings = queryset.filter(person=request.person)
        else:
            bookings = queryset
        serializer = RoomBookingSerializer(bookings, many=True)
        return Response(serializer.data)

    def partial_update(self, request, hostel__code, pk=None):
        data = request.data
        instance = get_object_or_404(RoomBooking, pk=pk)
        if 'status' in data.keys():
            if data['status'] == statuses.FORWARDED and \
                    not is_supervisor(request.person):
                return Response(
                    "Only Supervisor is allowed to perform this action!",
                    status=status.HTTP_403_FORBIDDEN,
                )
            elif not is_supervisor(request.person):
                return Response(
                    "Only Warden is allowed to perform this action!",
                    status=status.HTTP_403_FORBIDDEN,
                )
            elif not self.is_valid(data['status'], instance.status):
                return Response(
                    "Invalid action!",
                    status=status.HTTP_403_FORBIDDEN,
                )

        serializer = RoomBookingSerializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def is_valid(self, new_status, prev_status):
        """
        Checks to ensure the proper flow of statuses:
        1. Only forwarded request can be approved.
        2. Only pending request can be forwarded.
        3. Status of a rejected request can't be changed.
        """

        if prev_status == statuses.REJECTED or prev_status == statuses.APPROVED:
            return False
        if new_status == statuses.FORWARDED:
            return prev_status == statuses.PENDING
        if new_status == statuses.APPROVED:
            return prev_status == statuses.FORWARDED
        return True