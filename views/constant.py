import swapper

from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from bhawan_app.constants import (
    designations,
    complaint_types,
    statuses,
    days,
)

Hostel = swapper.load_model('Kernel', 'Residence')
Branch = swapper.load_model('Kernel', 'Branch')


class ConstantViewset(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """
    List view for constants and their codes
    """
    renderer_classes = [JSONRenderer,]

    def list(self, request):
        """
        Return JSONified dictionary of constants and corresponding codes.
        :return: dictionay of contants and codes
        """
        mapping = designations.STUDENT_COUNCIL_MAP
        reverse_student_council_map = \
            {mapping[key]: key for key in mapping.keys()}
        mapping = designations.ADMINISTRATIVE_COUNCIL_MAP
        reverse_administrative_council_map = \
            {mapping[key]: key for key in mapping.keys()}
        mapping = designations.GLOBAL_COUNCIL_MAP
        reverse_global_council_map = \
            {mapping[key]: key for key in mapping.keys()}
        mapping = complaint_types.COMPLAINT_TYPES_MAP
        reverse_complaint_types_map = \
            {mapping[key]: key for key in mapping.keys()}
        mapping = statuses.COMLAINT_STATUSES_MAP
        reverse_complaint_statuses_map = \
            {mapping[key]: key for key in mapping.keys()}
        mapping = statuses.BOOKING_STATUSES_MAP
        reverse_booking_statuses_map = \
            {mapping[key]: key for key in mapping.keys()}
        mapping = statuses.FEE_TYPES_MAP
        reverse_fee_types_map = \
            {mapping[key]: key for key in mapping.keys()}
        mapping = days.DAYS_MAP
        reverse_days = \
            {mapping[key]: key for key in mapping.keys()}

        response = {}
        response['designations'] = {
            **reverse_student_council_map,
            **reverse_administrative_council_map,
            **reverse_global_council_map,
        }
        response['global_council'] = designations.GLOBAL_COUNCIL_LIST
        response['student_council'] = designations.STUDENT_COUNCIL_LIST
        response['administrative_council'] = designations.ADMINISTRATIVE_COUNCIL_LIST
        response['complaint_types'] = reverse_complaint_types_map
        response['statues'] = {
            'COMLAINT_STATUSES': reverse_complaint_statuses_map,
            'BOOKING_STATUSES': reverse_booking_statuses_map,
            'FEE_TYPES': reverse_fee_types_map,
        }
        response['days'] = reverse_days

        hostels = Hostel.objects.all()
        response['hostels'] = {
            hostel.code: hostel.name for hostel in hostels
        }
        branches = Branch.objects.values('name', 'code')
        response['branches'] = {
            branch['code']: branch['name'] for branch in branches
        }
        return Response(response)
