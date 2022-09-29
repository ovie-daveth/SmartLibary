from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_page, name='profilepage'),
    path('create_profile', views.create_profile, name='profiles'),
]