from datetime import datetime

from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404

from bhawan_app.models import Complaint
from bhawan_app.serializers.complaint import ComplaintSerializer
from bhawan_app.managers.services import is_warden, is_supervisor   


class ComplaintViewset(viewsets.ModelViewSet):
    """
    Detail view for getting complaint information of a single hostel
    """

    serializer_class = ComplaintSerializer
    allowed_methods = ['GET', 'POST', 'PATCH']
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Complaint.objects.filter(
            person__residentialinformation__residence__code= \
                self.kwargs["hostel__code"],
        ).order_by('-datetime_modified')
        return queryset

    def get_serializer_context(self):
        return {
            "person": self.request.person,
        }

    def retrieve(self, request, hostel__code, pk=None):
        queryset = self.get_queryset()
        try:
            complaint = queryset.get(pk=pk)
        except ObjectDoesNotExist:
            complaint = Complaint.objects.none()
        serializer = ComplaintSerializer(complaint)
        return Response(serializer.data)
    
    def partial_update(self, request, hostel__code, pk=None):
        instance = get_object_or_404(Complaint, pk=pk)
        if not is_warden(request.person) and \
                not is_supervisor(request.person):
            return Response(
                "Only Supervisor and Warden are allowed to perform this action!",
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = ComplaintSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(datetime_modified=datetime.now())
        return Response(serializer.data)