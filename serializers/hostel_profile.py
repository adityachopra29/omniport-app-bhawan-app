from rest_framework import serializers

from bhawan_app.models import HostelProfile


class HostelProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for HostelProfile objects
    """

    hostel = serializers.CharField(source='hostel.name')

    class Meta:
        """
        Meta class for HostelProfileSerializer
        """

        model = HostelProfile
        fields = [
            'hostel',
            'description',
            'homepage_url',
            'display_picture',
        ]
