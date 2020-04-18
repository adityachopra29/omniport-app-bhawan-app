from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from bhawan_app.constants import (
    designations,
    complaint_types,
    statuses,
    days,
)

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
        
        response = {}
        response['designations'] = {
            'STUDENT_COUNCIL': designations.STUDENT_COUNCIL_MAP,
            'ADMINISTRATIVE_COUNCIL': designations.ADMINISTRATIVE_COUNCIL_MAP,
        }
        response['complaint_types'] = complaint_types.COMPLAINT_TYPES_MAP
        response['statues'] = {
            'COMLAINT_STATUSES': statuses.COMLAINT_STATUSES_MAP,
            'BOOKING_STATUSES': statuses.BOOKING_STATUSES_MAP,
        }
        response['days'] = days.DAYS_MAP
        return Response(response)
