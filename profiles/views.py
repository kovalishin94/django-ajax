from django.shortcuts import render
from .models import *
from django.http import JsonResponse, HttpResponse


def index(request):
    return render(request, 'profiles/index.html', {'content': 'List of Profiles'})

def getProfiles(request):
    profiles = Profile.objects.all()
    return JsonResponse({'profiles':list(profiles.values())})


def create(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        newProfile = Profile(name=name, e_mail=email)
        newProfile.save()
        return HttpResponse('New Profile created succesfully')
    
