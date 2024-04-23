from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=75, blank=False, default='')
    description = models.CharField(max_length=200)
    author = models.CharField(max_length=75, blank=False, default='')
    category = models.CharField(max_length=75, blank=False)