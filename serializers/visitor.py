from rest_framework import serializers

from bhawan_app.models import Visitor


class VisitorSerializer(serializers.ModelSerializer):
    """
    Serializer for Visitor objects
    """

    full_name = serializers.CharField(
        source='person.full_name',
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

    def create(self, validated_data):
        person, created = Visitor.objects.get_or_create(
           full_name=validated_data['full_name']
        )
        validated_data['person'] = person
        return super().create(validated_data)