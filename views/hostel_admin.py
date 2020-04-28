import swapper

from rest_framework import viewsets, status
from rest_framework.response import Response

from bhawan_app.models.roles.hostel_admin import HostelAdmin
from bhawan_app.serializers.hostel_admin import HostelAdminSerializer
from bhawan_app.constants import designations
from bhawan_app.pagination.custom_pagination import CustomPagination
from bhawan_app.managers.services import is_warden

Person = swapper.load_model('Kernel', 'Person')

class HostelAdminViewset(viewsets.ModelViewSet):
    """
    CRUD views for getting admin information of all hostels
    """

    serializer_class = HostelAdminSerializer
    allowed_methods = ['GET', 'POST', 'PATCH',]
    pagination_class = CustomPagination

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
                filters['designation__in'] = \
                    designations.STUDENT_COUNCIL_MAP.keys()

        """
        Filter based on hostel
        """
        filters['person__residentialinformation__residence__code']= \
                self.kwargs['hostel__code']
        return filters

    def partial_update(self, request, hostel__code, pk=None):
        if is_warden(request.person):
            instance = self.get_object()
            serializer = self.get_serializer(
                instance,
                data=request.data,
                partial=True,
            )
            serializer.is_valid(raise_exception=True)
            if 'person' in request.data.keys():
                person = Person.objects.get(pk=request.data['person'])
                serializer.save(person=person)
            else:
                serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(
            'Only warden is allowed to perform this action !',
            status=status.HTTP_403_FORBIDDEN,
        )