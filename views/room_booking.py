import json
import swapper
from datetime import datetime

from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from bhawan_app.models import RoomBooking, Visitor
from bhawan_app.serializers.room_booking import RoomBookingSerializer
from bhawan_app.managers.services import is_hostel_admin, is_supervisor, is_warden
from bhawan_app.constants import statuses

Person = swapper.load_model('kernel', 'Person')
ResidentialInformation = swapper.load_model('kernel', 'ResidentialInformation')


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
        queryset = RoomBooking.objects\
            .filter(**filters)\
            .order_by('-datetime_modified')
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
        if not is_hostel_admin(request.person):
            queryset = queryset.filter(person=request.person)
        serializer = RoomBookingSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, hostel__code):
        file_data = self.request.FILES
        visitors = self.request.POST.pop('visitors')
        try:
            residential_information = request.person.residentialinformation
        except ResidentialInformation.DoesNotExist:
            return Response(
                f'{request.person}\'s residential informarion is not registered',
                status=status.HTTP_403_FORBIDDEN,
            )
        try:
            visitor_index = 0
            for visitor in visitors:
                sanitized_data = {}
                for data in self.request.POST:
                    sanitized_data[data] = self.request.POST[data]
                room_booking = RoomBooking.objects.create(
                    person=request.person,
                    **sanitized_data,
                )
                visitor = json.loads(visitor)
                visitor_full_name = visitor.pop('full_name')
                visitor_person = Person.objects.create(
                    full_name=visitor_full_name,
                )
                photo_identification = file_data.pop(f'visitors_{visitor_index}')
                Visitor.objects.create(
                    person=visitor_person,
                    photo_identification=photo_identification,
                    booking=room_booking, **visitor,
                )
                visitor_index+=1
            return Response(
                'Room booking requested',
                status=status.HTTP_201_CREATED,
            )
        except Exception as error:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)


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
            elif not is_warden(request.person):
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
        serializer.save(datetime_modified=datetime.now())
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