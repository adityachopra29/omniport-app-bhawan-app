from django.urls import path

from bhawan_app.views.hello_world import HelloWorld
from bhawan_app.views.hostel_profile import HostelProfileList

app_name = 'bhawan_app'

urlpatterns = [
    path('', HelloWorld.as_view(), name='hello_world'),
    path(
        'hostel_profile/',
        HostelProfileList.as_view(),
        name='hostel_profile_list',
    ),
]
