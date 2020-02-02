from rest_framework import generics

from bhawan_app.models import Facility
from bhawan_app.serializers.facility import FacilitySerializer


class FacilityListView(generics.ListAPIView):
    """
    Detail view for getting facility information of a single hostel
    """

    serializer_class = FacilitySerializer
    lookup_field = 'hostel__code'

    def get_queryset(self):
        """
        Return the queryset of facilities of a hostel
        :return: the queryset of facilities of a hostel
        """

        hostel = self.kwargs['hostel__code']
        queryset = Facility.objects.filter(hostel__code=hostel)

        return queryset
