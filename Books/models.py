from email.policy import default
from django.db import models

class Genres(models.Model):
    topic = models.CharField(max_length = 100)

    def __str__(self):
        return self.topic

class Books(models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)
    price = models.IntegerField()
    genre = models.ForeignKey(Genres, on_delete=models.SET_NULL, null=True)
    available = models.BooleanField(default= True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title