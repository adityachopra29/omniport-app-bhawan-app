from rest_framework import serializers

from bhawan_app.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for Profile objects
    """

    hostel = serializers.CharField(source='hostel.name')

    class Meta:
        """
        Meta class for ProfileSerializer
        """

        model = Profile
        fields = [
            'id',
            'hostel',
            'description',
            'homepage_url',
            'display_picture',
        ]
