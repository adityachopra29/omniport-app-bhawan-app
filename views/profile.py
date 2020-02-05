from rest_framework import viewsets, mixins

from bhawan_app.models import Profile
from bhawan_app.serializers.profile import ProfileSerializer


class ProfileViewset(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """
    List view for getting profile information of all hostels
    """

    serializer_class = ProfileSerializer


    def get_queryset(self):
        """
        Return the queryset of profile grouped by a hostel
        :return: the queryset of profile grouped by a hostel
        """

        queryset = Profile.objects.filter(
            hostel__code=self.kwargs['hostel__code'],
        )
        return queryset
