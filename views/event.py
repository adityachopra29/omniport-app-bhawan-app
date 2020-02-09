from rest_framework import viewsets, mixins

from bhawan_app.models import Event
from bhawan_app.serializers.event import EventSerializer


class EventViewset(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """
    Detail view for getting event information of a single hostel
    """

    serializer_class = EventSerializer

    def get_queryset(self):
        """
        Return the queryset of events of a hostel
        :return: the queryset of events of a hostel
        """

        hostel_code = self.kwargs['hostel__code']
        queryset = Event.objects.filter(hostel__code=hostel_code)

        return queryset
    