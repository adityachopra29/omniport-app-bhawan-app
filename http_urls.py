from django.urls import path

from bhawan_app.views.hello_world import HelloWorld

app_name = 'bhawan_app'

urlpatterns = [
    path('', HelloWorld.as_view(), name='hello_world'),
]
