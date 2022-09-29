from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload, name='upload'),
    path('libary', views.libary, name='libary'),
    path('my_libary', views.my_libary, name='my-libary'),
    path('delete', views.delete, name='delete'),
]
