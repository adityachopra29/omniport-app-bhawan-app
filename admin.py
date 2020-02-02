from omniport.admin.site import omnipotence

from bhawan_app.models import (
    Profile,
    Contact,
    Facility,
    RoomBooking,
    Visitor,
    Complaint,
)

from bhawan_app.models.roles import Admin

omnipotence.register(Profile)
omnipotence.register(Contact)
omnipotence.register(Facility)
omnipotence.register(RoomBooking)
omnipotence.register(Visitor)
omnipotence.register(Complaint)
omnipotence.register(Admin)
