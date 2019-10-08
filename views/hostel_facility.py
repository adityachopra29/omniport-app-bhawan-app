from rest_framework import generics

from bhawan_app.models import HostelFacility
from bhawan_app.serializers.hostel_facility import HostelFacilitySerializer


class HostelFacilityListView(generics.ListAPIView):
    """
    Detail view for getting facility information of a single hostel
    """

    serializer_class = HostelFacilitySerializer
    lookup_field = 'hostel__code'

    def get_queryset(self):
        """
        Return the queryset of facilities of a hostel
        :return: the queryset of facilities of a hostel
        """

        hostel = self.kwargs['hostel__code']
        queryset = HostelFacility.objects.filter(hostel__code=hostel)

        return queryset
