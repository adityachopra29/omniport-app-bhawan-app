from omniport.admin.site import omnipotence

from bhawan_app.models import (
    HostelProfile,
    HostelContact,
    HostelFacility,
)

omnipotence.register(HostelProfile)
omnipotence.register(HostelContact)
omnipotence.register(HostelFacility)
