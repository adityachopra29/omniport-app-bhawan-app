from omniport.admin.site import omnipotence

from bhawan_app.models import (
    HostelProfile,
    HostelContact,
    HostelFacility,
    HostelRoomBooking,
    HostelVisitor,
    HostelComplaint,
)

omnipotence.register(HostelProfile)
omnipotence.register(HostelContact)
omnipotence.register(HostelFacility)
omnipotence.register(HostelRoomBooking)
omnipotence.register(HostelVisitor)
omnipotence.register(HostelComplaint)
