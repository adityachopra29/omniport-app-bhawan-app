from django.urls import path, include
from rest_framework.routers import DefaultRouter

from bhawan_app.views.profile import ProfileViewset
from bhawan_app.views.contact import ContactViewset
from bhawan_app.views.facility import FacilityViewset
from bhawan_app.views.complaint import ComplaintViewset
from bhawan_app.views.room_booking import RoomBookingViewset
from bhawan_app.views.personal_info import PersonalInfoView
from bhawan_app.views.event import EventViewset


app_name = "bhawan_app"

router = DefaultRouter()

router.register(
    r"(?P<hostel__code>[\w\-]+)/complaint", ComplaintViewset, basename="complaint",
)
router.register(
    r"(?P<hostel__code>[\w\-]+)/room_booking",
    RoomBookingViewset,
    basename="room_booking",
)
router.register(
    r"(?P<hostel__code>[\w\-]+)/facility", FacilityViewset, basename="facility",
)
router.register(
    r"(?P<hostel__code>[\w\-]+)/profile", ProfileViewset, basename="profle",
)
router.register(
    r"(?P<hostel__code>[\w\-]+)/contact", ContactViewset, basename="contact",
)
router.register(
    r"(?P<hostel__code>[\w\-]+)/event", EventViewset, basename="event",
)

urlpatterns = [
    path(
        'personal_info/',
        PersonalInfoView.as_view(),
        name='personal_info',
    ),
]


urlpatterns += router.urls
