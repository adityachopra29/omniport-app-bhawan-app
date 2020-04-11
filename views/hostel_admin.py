from rest_framework import viewsets

from bhawan_app.models.roles.hostel_admin import HostelAdmin
from bhawan_app.serializers.hostel_admin import HostelAdminSerializer
from bhawan_app.constants import designations

class HostelAdminViewset(viewsets.ModelViewSet):
    """
    List view for getting admin information of all hostels
    """

    serializer_class = HostelAdminSerializer
    allowed_methods = ['GET',]

    def get_queryset(self):
        """
        Return the queryset of profile grouped by a hostel
        :return: the queryset of profile grouped by a hostel
        """
        filters = {}
        if 'student' in self.request.GET.keys():
            if self.request.GET['student'] == 'true':
                filters['designation__in'] = designations.STUDENT_POSTS
        filters['person__residentialinformation__residence__code'] = \
            self.kwargs["hostel__code"]
        queryset = HostelAdmin.objects.filter(**filters)
        return queryset
