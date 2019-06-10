from rest_framework import generics

from bhawan_app.models import HostelContact
from bhawan_app.serializers.hostel_contact import HostelContactSerializer


class HostelContactDetailView(generics.ListAPIView):
    """
    Detail view for getting contact information of a single hostel
    """

    serializer_class = HostelContactSerializer
    lookup_field = 'hostel__code'

    def get_queryset(self):
        """
        Return the queryset of contacts of a hostel
        :return: the queryset of contacts of a hostel
        """

        hostel = self.kwargs['hostel__code']
        queryset = HostelContact.objects.filter(hostel__code=hostel)

        return queryset
