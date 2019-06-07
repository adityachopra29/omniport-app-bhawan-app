from rest_framework import generics

from bhawan_app.models import HostelProfile
from bhawan_app.serializers.hostel_profile import HostelProfileSerializer

class HostelProfileList(generics.ListAPIView):
    """
    List view for getting profile information of all hostels
    """

    queryset = HostelProfile.objects.all()
    serializer_class = HostelProfileSerializer
