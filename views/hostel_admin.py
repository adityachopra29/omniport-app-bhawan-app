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
        filters = self.get_filters(self.request)
        queryset = HostelAdmin.objects.filter(**filters)
        return queryset

    def get_filters(self, request):
        """
        Return a dict with all the filters populated with the
        filters received from query params.
        """
        filters = {}
        params = self.request.GET
        
        """
        Apply the filters for statuses.
        Usage: /admin/?student=true gives all hostel admins which are 
        students.
        """
        if 'student' in params.keys():
            student = params['student']
            if student == 'true':
                filters['designation__in'] = designations.STUDENT_POSTS.keys()

        """
        Filter based on hostel
        """
        filters['person__residentialinformation__residence__code']= \
                self.kwargs['hostel__code']
        return filters