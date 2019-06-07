from rest_framework import generics

from bhawan_app.models import HostelContact
from bhawan_app.serializers.hostel_contact import HostelContactSerializer


class HostelContactDetailView(generics.ListAPIView):
    """
    Detail view for getting contact information of a single hostel
    """

    serializer_class = HostelContactSerializer

    def get_queryset(self):
        """
        Return the queryset of contacts of a hostel
        :return: the queryset of contacts of a hostel
        """

        hostel = self.request.query_params.get('code')
        if hostel:
            queryset = HostelContact.objects.filter(hostel__code=hostel)
        else:
            queryset = HostelContact.objects.none()

        return queryset
