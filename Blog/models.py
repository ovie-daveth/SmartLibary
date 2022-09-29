from django.db import models

class Aspect(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

class Blog(models.Model):
    Title = models.CharField(max_length=100)
    #author
    #pic
    #video = models.FileField(upload_to=)
    aspect = models.ForeignKey(Aspect, on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=1000)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Title


