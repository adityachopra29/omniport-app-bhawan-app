from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist


from bhawan_app.models import Complaint
from bhawan_app.permissions.is_owner import IsOwner
from bhawan_app.permissions.is_hostel_admin import IsHostelAdmin
from bhawan_app.permissions.is_supervisor import IsSupervisor
from bhawan_app.serializers.complaint import ComplaintSerializer


class ComplaintViewset(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """
    Detail view for getting complaint information of a single hostel
    """

    permission_classes = [IsOwner|IsHostelAdmin]
    serializer_class = ComplaintSerializer

    def get_queryset(self):
        queryset = Complaint.objects.filter(hostel__code=self.kwargs["hostel__code"],)
        return queryset

    def retrieve(self, request, hostel__code, pk):
        queryset = self.get_queryset()
        try:
            complaint = queryset.get(pk=pk)
            self.check_object_permissions(request, complaint.person)
        except ObjectDoesNotExist:
            complaint = None
        serializer = ComplaintSerializer(complaint)
        return Response(serializer.data)

    def get_serializer_context(self):
        return {
            "person": self.request.person,
            "hostel__code": self.kwargs["hostel__code"],
        }

    @action(
        detail=True,
        methods=["POST", "GET"],
        permission_classes=[IsSupervisor],
        url_path="forward",
    )
    def forward(self, request, hostel__code, pk=None):
        obj = self.get_object()
        # obj.forwarded =
