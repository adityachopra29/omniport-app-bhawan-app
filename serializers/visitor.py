import swapper

from rest_framework import serializers

from bhawan_app.models import Visitor

Person = swapper.load_model('Kernel', 'Person')

class VisitorSerializer(serializers.ModelSerializer):
    """
    Serializer for Visitor objects
    """

    full_name = serializers.CharField(
        source='person.full_name',
        read_only=True
    )
    class Meta:
        """
        Meta class for ProfileSerializer
        """

        model = Visitor
        fields = [
            'id',
            'full_name',
            'relation',
            'photo_identification',
        ]