from django.shortcuts import render
from SmartLibary.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
# Create your views here.

def profile_page(request):
    return render(request, 'profiles/profile_page.html')

def create_profile(request):
    return render(request, 'profiles/create_profile.html')