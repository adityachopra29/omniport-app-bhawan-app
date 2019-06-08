from django.urls import path

from bhawan_app.views.hostel_profile import (
    HostelProfileListView,
    HostelProfileDetailView,
)
from bhawan_app.views.hostel_contact import HostelContactDetailView

app_name = 'bhawan_app'

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
        'hostel_contact/',
        HostelContactDetailView.as_view(),
        name='hostel_contact_detail',
    ),
]
