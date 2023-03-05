from django.urls import path
from profiles.views import *

urlpatterns = [
    path('', index, name='home'),
    path('getProfiles', getProfiles, name='getProfiles'),
    path('create', create, name='createProfiles'),
]
