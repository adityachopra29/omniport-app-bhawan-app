import swapper

from rest_framework import serializers

from bhawan_app.models import HostelComplaint 

class HostelComplaintSerializer(serializers.ModelSerializer):
    """
    Serializer for HostetComplaint objects
    """

    hostel = serializers.CharField(
        source='hostel.name',
        read_only=True,
    )

    hostel_code = serializers.CharField(
        source='hostel.code'
    )

    class Meta:
        model = HostelComplaint
        fields = [
            'hostel',
            'complainant',
            'status',
            'complaint_type',
            'available_from',
            'available_till',
            'room_no',
            'hostel_code',
            'description',
        ]
        read_only_field = [
            'hostel',
        ]

    def create(self, validated_data):
        Residence = swapper.load_model('Kernel', 'Residence')
        hostel_code = validated_data['hostel']['code']
        hostel = Residence.objects.get(code=hostel_code)
        validated_data['hostel'] = hostel
        return super().create(validated_data)