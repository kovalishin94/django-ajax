from django.shortcuts import render
from .models import *
from django.http import JsonResponse


def index(request):
    return render(request, 'profiles/index.html', {'content': 'List of Profiles'})

def getProfiles(request):
    profiles = Profile.objects.all()
    return JsonResponse({'profiles':list(profiles.values())})


def create(request):
    pass
