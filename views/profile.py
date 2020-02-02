from rest_framework import generics

from bhawan_app.models import Profile
from bhawan_app.serializers.profile import ProfileSerializer


class ProfileListView(generics.ListAPIView):
    """
    List view for getting profile information of all hostels
    """

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetailView(generics.RetrieveAPIView):
    """
    Detail view for getting profile information of a single hostel
    """

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'hostel__code'
