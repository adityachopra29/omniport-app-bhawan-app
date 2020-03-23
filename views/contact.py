from rest_framework import mixins, viewsets

from bhawan_app.models import Contact
from bhawan_app.serializers.contact import ContactSerializer


class ContactViewset(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """
    Detail view for getting contact information of a single hostel
    """

    serializer_class = ContactSerializer

    def get_queryset(self):
        """
        Return the queryset of contacts of a hostel
        :return: the queryset of contacts of a hostel
        """

        hostel = self.kwargs["hostel__code"]
        queryset = Contact.objects.filter(hostel__code=hostel)

        return queryset
