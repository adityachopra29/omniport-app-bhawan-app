import swapper
from rest_framework import serializers

from formula_one.models.generics.contact_information import ContactInformation

from bhawan_app.models import Complaint


class ComplaintSerializer(serializers.ModelSerializer):
    """
    Serializer for Complaint objects
    """

    complainant = serializers.CharField(
        source='person.full_name',
    )
    hostel_code = serializers.CharField(
        source='person.residentialinformation.residence.code',
        read_only=True,
    )
    room_no = serializers.CharField(
        source='person.residentialinformation.room_number',
        read_only=True,
    )

    phone_number = serializers.SerializerMethodField()

    class Meta:
        model = Complaint
        fields = [
            "complainant",
            "status",
            "complaint_type",
            "room_no",
            "hostel_code",
            "description",
            "id",
            "phone_number",
        ]
        extra_kwargs = {
            "person": {"read_only": True},
        }

    def create(self, validated_data):
        Hostel = swapper.load_model('kernel', 'Residence')
        hostel_code = self.context['hostel__code']
        try:
            hostel = Hostel.objects.get(code=hostel_code)
        except Exception:
            raise serializers.ValidationError("Wrong hostel code")
        validated_data["person"] = self.context["person"]
        validated_data["hostel"] = hostel
        return super().create(validated_data)

    def get_phone_number(self, obj):
        """
        Returns the primary phone number of the complainant
        :return: the primary phone number of the complainant
        """

        try:
            contact_information = \
                ContactInformation.objects.get(person=obj.person)
            return contact_information.primary_phone_number
        except ContactInformation.DoesNotExist:
            return None
