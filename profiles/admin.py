from django.contrib import admin
from profiles.models import *


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display = ['name', 'e_mail']
