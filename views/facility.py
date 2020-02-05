from rest_framework import viewsets, mixins

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

    def get_queryset(self):
        """
        Return the queryset of facilities of a hostel
        :return: the queryset of facilities of a hostel
        """

        hostel = self.kwargs['hostel__code']
        queryset = Facility.objects.filter(hostel__code=hostel)

        return queryset
    