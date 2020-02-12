import swapper
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from bhawan_app.models import Facility
from bhawan_app.serializers.facility import FacilitySerializer

class FacilityViewset(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """
    Detail view for getting facility information of a single hostel
    """

    serializer_class = FacilitySerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        """
        Return the queryset of facilities of a hostel
        :return: the queryset of facilities of a hostel
        """

        hostel = self.kwargs['hostel__code']
        queryset = Facility.objects.filter(hostel__code=hostel)

        return queryset

    def get_serializer_context(self):
        return {
            "hostel__code": self.kwargs['hostel__code'],
        }