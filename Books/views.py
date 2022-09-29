from django.shortcuts import render

from SmartLibary.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
# Create your views here.

def upload(request):
    return render(request, 'Books/upload.html')

def libary(request):
    return render(request, 'Books/libary.html')

def my_libary(request):
    return render(request, 'Blog/my_libary.html.html')

def delete(request):
    return render(request, 'Blog/delete.html')
