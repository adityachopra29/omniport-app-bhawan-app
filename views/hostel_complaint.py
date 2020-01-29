from rest_framework import mixins, viewsets

from bhawan_app.models import HostelComplaint
from bhawan_app.serializers.hostel_complaint import HostelComplaintSerializer


class HostelComplaintViewset(viewsets.ModelViewset):
    """
    Detail view for getting complaint information of a single hostel
    """

    serializer_class = HostelComplaintSerializer
    queryset = HostelComplaint.objects.all() 

    def list(self, reqeust, pr=None):
        print(self.kwargs['bhawan__code'], "*"*50)
        return super().list(reqeust, pk)