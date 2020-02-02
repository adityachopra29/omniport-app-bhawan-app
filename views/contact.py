from rest_framework import generics

from bhawan_app.models import Contact
from bhawan_app.serializers.contact import ContactSerializer


class ContactListView(generics.ListAPIView):
    """
    Detail view for getting contact information of a single hostel
    """

    serializer_class = ContactSerializer
    lookup_field = 'hostel__code'

    def get_queryset(self):
        """
        Return the queryset of contacts of a hostel
        :return: the queryset of contacts of a hostel
        """

        hostel = self.kwargs['hostel__code']
        queryset = Contact.objects.filter(hostel__code=hostel)

        return queryset
