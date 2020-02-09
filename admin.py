from omniport.admin.site import omnipotence

from bhawan_app.models import (
    Profile,
    Contact,
    Facility,
    RoomBooking,
    Complaint,
    Timing,
    Relative,
    Event,
)

from bhawan_app.models.roles import HostelAdmin

omnipotence.register(Profile)
omnipotence.register(Contact)
omnipotence.register(Facility)
omnipotence.register(RoomBooking)
omnipotence.register(Complaint)
omnipotence.register(HostelAdmin)
omnipotence.register(Timing)
omnipotence.register(Relative)
omnipotence.register(Event)

