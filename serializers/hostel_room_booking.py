import swapper

from rest_framework import serializers

from bhawan_app.models import HostelRoomBooking 

class HostelRoomBookingSerializer(serializers.ModelSerializer):
    """
    Serializer for HostelRoomBooking objects
    """
    hostel = serializers.CharField(
        source='hostel.name'
    )

    hostel_code = serializers.CharField(
        source='hostel.code'
    )

    class Meta:
        model = HostelRoomBooking
        fields = [
            'hostel',
            'filer',
            'status',
            'requested_from',
            'requested_till',
            'room_no_of_filer',
            'hostel_code',
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