from django.urls import path, include
from rest_framework.routers import DefaultRouter

from bhawan_app.views.profile import ProfileViewset
from bhawan_app.views.contact import ContactViewset
from bhawan_app.views.facility import FacilityViewset
from bhawan_app.views.complaint import ComplaintViewset
from bhawan_app.views.room_booking import RoomBookingViewset
from bhawan_app.views.personal_info import PersonalInfoView
from bhawan_app.views.event import EventViewset


app_name = 'bhawan_app'

router = DefaultRouter()

router.register(
    r'complaint/(?P<hostel__code>[\w\-]+)',
    ComplaintViewset,
    basename='complaint',
)
router.register(
    r'room_booking/(?P<hostel__code>[\w\-]+)',
    RoomBookingViewset,
    basename='room_booking',
)
router.register(
    r'facility/(?P<hostel__code>[\w\-]+)',
    FacilityViewset,
    basename='facility',
)
router.register(
    r'profile/(?P<hostel__code>[\w\-]+)',
    ProfileViewset,
    basename='profle',
)
router.register(
    r'contact/(?P<hostel__code>[\w\-]+)',
    ContactViewset,
    basename='contact',
)
router.register(
    r'event/(?P<hostel__code>[\w\-]+)',
    EventViewset,
    basename='event',
)

urlpatterns = [
    path(
        'personal_info/',
        PersonalInfoView.as_view(),
        name='personal_info',
    ),
]


urlpatterns += router.urls
