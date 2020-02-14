import swapper

from rest_framework import serializers

from bhawan_app.models import Complaint


class ComplaintSerializer(serializers.ModelSerializer):
    """
    Serializer for Complaint objects
    """

    hostel = serializers.CharField(
        source='hostel.name',
        read_only=True,
    )

    hostel_code = serializers.CharField(
        source='hostel.code',
        read_only=True,
    )

    class Meta:
        model = Complaint
        fields = [
            'hostel',
            'person',
            'status',
            'complaint_type',
            'available_from',
            'available_till',
            'room_no',
            'hostel_code',
            'description',
            'id',
        ]
        extra_kwargs = {
            'person': {'read_only': True},
        }

    def create(self, validated_data):
        Hostel = swapper.load_model('kernel', 'Residence')
        hostel_code = self.context['hostel__code']
        try:
            hostel = Hostel.objects.get(code=hostel_code)
        except Exception:
            raise serializers.ValidationError('Wrong hostel code')
        validated_data['person'] = self.context['person']
        validated_data['hostel'] = hostel
        return super().create(validated_data)
