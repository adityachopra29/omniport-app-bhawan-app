from rest_framework import serializers

from bhawan_app.models import Relative


class RelativeSerializer(serializers.ModelSerializer):
    """
    Serializer for Relative objects
    """

    class Meta:
        """
        Meta class for ProfileSerializer
        """

        model = Relative
        fields = [
            'id',
            'name',
            'relation',
        ]