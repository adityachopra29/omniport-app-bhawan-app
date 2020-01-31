from django.urls import path, include
from rest_framework.routers import DefaultRouter

from bhawan_app.views.hostel_profile import (
    HostelProfileListView,
    HostelProfileDetailView,
)
from bhawan_app.views.hostel_contact import HostelContactListView
from bhawan_app.views.hostel_facility import HostelFacilityListView
from bhawan_app.views.hostel_complaint import HostelComplaintViewset
from bhawan_app.views.hostel_room_booking import HostelRoomBookingViewset

app_name = 'bhawan_app'

router = DefaultRouter()
router.register(r'hostel_complaint/(?P<hostel__code>[\w\-]+)', HostelComplaintViewset, basename='HostelComplaint')
router.register(r'hostel_room_booking/(?P<hostel__code>[\w\-]+)', HostelRoomBookingViewset, basename='HostelRoomBooking')

    
urlpatterns = [
    path(
        'hostel_profile/',
        HostelProfileListView.as_view(),
        name='hostel_profile_list',
    ),
    path(
        'hostel_profile/<hostel__code>',
        HostelProfileDetailView.as_view(),
        name='hostel_profle_detail',
    ),
    path(
        'hostel_contact/<hostel__code>',
        HostelContactListView.as_view(),
        name='hostel_contact_detail',
    ),
    path(
        'hostel_facility/<hostel__code>',
        HostelFacilityListView.as_view(),
        name='hostel_facility_list',
    ),
]

urlpatterns += router.urls
