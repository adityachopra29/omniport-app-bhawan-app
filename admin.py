from omniport.admin.site import omnipotence

from bhawan_app.models import (
    HostelProfile,
    HostelContact,
)

omnipotence.register(HostelProfile)
omnipotence.register(HostelContact)
