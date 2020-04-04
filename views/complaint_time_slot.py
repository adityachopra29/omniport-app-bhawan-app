from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from bhawan_app.models import ComplaintTimeSlot
from bhawan_app.permissions.is_hostel_admin import IsHostelAdmin
from bhawan_app.serializers.complaint_time_slot import (
    ComplaintTimeSlotSerializer
)


class ComplaintTimeSlotViewset(viewsets.ModelViewSet):
    """
    Viewset for performing CRUD operations on time slots of complaints
    """

    queryset = ComplaintTimeSlot.objects.all()
    serializer_class = ComplaintTimeSlotSerializer
    permission_classes = [IsAuthenticated|IsHostelAdmin]
