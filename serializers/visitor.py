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
    full_name = serializers.CharField(
        write_only=True,
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
            'full_name',
        ]

    def create(self, validated_data):
        person, created = Person.objects.get_or_create(
           full_name=validated_data['full_name'],
        )
        validated_data.pop('full_name')
        validated_data['person'] = person
        return super().create(validated_data)