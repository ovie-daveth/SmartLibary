from django.shortcuts import render

# Create your views here.

def signup(request):
    return render(request, 'UserAuth/signup.html')

def signin(request):
    return render(request, 'UserAuth/signin.html')

def signout(request):
    return render(request, 'UserAuth/signout.html')