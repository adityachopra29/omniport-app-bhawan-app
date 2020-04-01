import swapper

from rest_framework import status
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from bhawan_app.serializers.whoami import WhoAmISerializer

ResidentialInformation = swapper.load_model("Kernel", "ResidentialInformation")


class WhoAmIViewset(
    mixins.RetrieveModelMixin, viewsets.GenericViewSet,
):
    """
    This view shows some personal information of the currently logged in user
    """

    permission_classes = [
        IsAuthenticated,
    ]
    http_method_names = [
        "GET",
    ]

    def retrieve(self, request, pk=None):
        """
        View to serve GET requests
        :param request: the request that is to be responded to
        :param args: arguments
        :param kwargs: keyword arguments
        :return: the response for request
        """
        person = request.person
        residential_info = ResidentialInformation.objects.get(person=person)
        serializer = WhoAmISerializer(residential_info)
        return Response(serializer.data, status=status.HTTP_200_OK)
