from django.shortcuts import render
from SmartLibary.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT


def home(request):
    return render(request, 'Blog/index.html')

def blog(request):
    return render(request, 'Blog/blog.html')
