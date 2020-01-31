from rest_framework import mixins, viewsets
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist


from bhawan_app.models import HostelComplaint
from bhawan_app.permissions.is_owner_or_admin import IsOwnerOrHostelAdmin
from bhawan_app.serializers.hostel_complaint import HostelComplaintSerializer


class HostelComplaintViewset(mixins.ListModelMixin,
                             mixins.CreateModelMixin,
                             mixins.RetrieveModelMixin,
                             viewsets.GenericViewSet):
    """
    Detail view for getting complaint information of a single hostel
    """

    permission_classes = [IsOwnerOrHostelAdmin]
    serializer_class = HostelComplaintSerializer

    def get_queryset(self):
        queryset = HostelComplaint.objects.filter(hostel__code=self.kwargs['hostel__code'])
        return queryset

    def retrieve(self, request, hostel__code, pk):
        queryset = self.get_queryset()
        try:
            complaint = queryset.get(pk=pk)
            self.check_object_permissions(request, complaint.complainant)
        except ObjectDoesNotExist:
            complaint = None
        serializer = HostelComplaintSerializer(complaint)
        return Response(serializer.data)