from django.db import models

# Create your models here.
class Nationality(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Userprofile(models.Model):
    firstname = models.CharField(max_length=100, blank=False)
    lasttname = models.CharField(max_length=100, blank=False)
    username = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    nationality = models.ForeignKey(Nationality, on_delete = models.SET_NULL, null=True)
    state = models.CharField(max_length=255, blank=False)
    picture = models.ImageField()
    is_vendor = models.BooleanField(default=False)
    is_reader = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username