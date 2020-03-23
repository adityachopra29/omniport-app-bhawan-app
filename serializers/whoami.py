import swapper

from rest_framework import serializers

from bhawan_app.managers.services import is_hostel_admin

ResidentialInformation = swapper.load_model("Kernel", "ResidentialInformation")


class WhoAmISerializer(serializers.ModelSerializer):
    """
    Serializer for ResidentialInformation objects
    """

    residence = serializers.CharField(source="residence.code",)

    is_admin = serializers.SerializerMethodField(read_only=True,)

    class Meta:
        """
        Meta class for WhoAmISerializer
        """

        model = ResidentialInformation
        fields = [
            "person",
            "residence",
            "room_number",
            "is_admin",
        ]

    def get_is_admin(self, obj):
        return is_hostel_admin(obj.person)
