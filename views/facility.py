import swapper
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from bhawan_app.models import Facility
from bhawan_app.serializers.facility import FacilitySerializer
from bhawan_app.pagination.custom_pagination import CustomPagination
from bhawan_app.managers.services import is_hostel_admin


class FacilityViewset(viewsets.ModelViewSet):
    """
    Detail view for getting facility information of a single hostel
    """

    serializer_class = FacilitySerializer
    permission_classes = [IsAuthenticated,]
    pagination_class = CustomPagination
    allowed_methods = ['GET', 'POST', 'PATCH']

    def get_queryset(self):
        """
        Return the queryset of facilities of a hostel
        :return: the queryset of facilities of a hostel
        """

        hostel = self.kwargs['hostel__code']
        queryset = Facility.objects.filter(hostel__code=hostel)

        return queryset

    def get_serializer_context(self):
        return {
            'hostel__code': self.kwargs['hostel__code'],
        }

    def create(self, request, hostel__code):
        """
        Create facility instance if user has required permissions.
        :return: new facility instance
        """
        if is_hostel_admin(request.person):
            return super().create(request, hostel__code)
            
        return Response(
            {"You are not allowed to perform this action !"},
            status=status.HTTP_403_FORBIDDEN,
        )
    
    def partial_update(self, request, hostel__code, pk=None):
        """
        Update facility instance if user has required permissions.
        :return: updated facility instance
        """
        if is_hostel_admin(request.person):
            return super().partial_update(request, hostel__code, pk)
            
        return Response(
            {"You are not allowed to perform this action !"},
            status=status.HTTP_403_FORBIDDEN,
        )