from django.db import models
from django.utils import timezone

class Project(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='projects/', default='projects/default.jpg', blank=True, null=True)
    summary = models.TextField()

class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateField(default=timezone.now)
