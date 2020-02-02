from django.urls import path, include
from rest_framework.routers import DefaultRouter

from bhawan_app.views.profile import (
    ProfileListView,
    ProfileDetailView,
)
from bhawan_app.views.contact import ContactListView
from bhawan_app.views.facility import FacilityListView
from bhawan_app.views.complaint import ComplaintViewset
from bhawan_app.views.room_booking import RoomBookingViewset

app_name = 'bhawan_app'

router = DefaultRouter()
router.register(r'complaint/(?P<hostel__code>[\w\-]+)', ComplaintViewset, basename='Complaint')
router.register(r'room_booking/(?P<hostel__code>[\w\-]+)', RoomBookingViewset, basename='RoomBooking')

    
urlpatterns = [
    path(
        'profile/',
        ProfileListView.as_view(),
        name='profile_list',
    ),
    path(
        'profile/<hostel__code>',
        ProfileDetailView.as_view(),
        name='hostel_profle_detail',
    ),
    path(
        'contact/<hostel__code>',
        ContactListView.as_view(),
        name='contact_detail',
    ),
    path(
        'facility/<hostel__code>',
        FacilityListView.as_view(),
        name='facility_list',
    ),
]

urlpatterns += router.urls
