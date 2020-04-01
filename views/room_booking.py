from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from bhawan_app.models import RoomBooking
from bhawan_app.permissions.is_owner import IsOwner
from bhawan_app.permissions.is_hostel_admin import IsHostelAdmin
from bhawan_app.serializers.room_booking import RoomBookingSerializer
from bhawan_app.managers.services import get_hostel_admin


class RoomBookingViewset(viewsets.ModelViewSet):

    """
    Detail view for getting contact information of a single hostel
    """

    serializer_class = RoomBookingSerializer

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
    

    def get_permissions(self):
        if 'forwarded' in self.request.GET.keys() and self.action == 'partial_update':
            permission_classes = [IsSupervisor, IsAuthenticated]
        else:
            permission_classes = [IsOwner|IsHostelAdmin, IsAuthenticated]
        return [permission() for permission in permission_classes]


    def list(self, request, hostel__code):
        """
        List all the bookings according to permissions
        """

        queryset = self.get_queryset()
        if get_hostel_admin(request.user.person) is None:
            bookings = queryset.filter(person=request.person)
        else:
            bookings = queryset
        serializer = RoomBookingSerializer(bookings, many=True)
        return Response(serializer.data)


    def partial_update(self, request, hostel__code, pk=None):
        instance = RoomBooking.objects.get(pk=pk)
        serializer = RoomBookingSerializer(instance, data=self.request.POST, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)