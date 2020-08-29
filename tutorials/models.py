from django.db import models
from django.utils import timezone

# Create your models here.

class Tutorial(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='tutorials', blank=True)
    description = models.TextField(blank=True)
    def __str__ (self):
        return self.name

class Topic(models.Model):
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='topics', blank=True)
    vedio_link = models.URLField(blank=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

