from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from bhawan_app.models import RoomBooking
from bhawan_app.serializers.room_booking import RoomBookingSerializer
from bhawan_app.managers.services import get_hostel_admin, is_supervisor, is_warden


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
        filters['hostel__code'] = self.kwargs['hostel__code']
        if 'forwarded' in self.request.GET.keys():
            filters['forwarded'] = self.request.GET['forwarded']
        queryset = RoomBooking.objects.filter(**filters)
        return queryset


    def get_serializer_context(self):
        return {
            "hostel__code": self.kwargs["hostel__code"],
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
        if 'forwarded' in data.keys() and not is_supervisor(request.person):
                return Response("Only Supervisor is allowed to perform this action!", status=status.HTTP_403_FORBIDDEN)

        if 'status' in data.keys() and not is_warden(request.person):
                return Response("Only Warden is allowed to perform this action!", status=status.HTTP_403_FORBIDDEN)
        
        instance = RoomBooking.objects.get(pk=pk)
        serializer = RoomBookingSerializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)