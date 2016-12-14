from django.db import models

# Create your models here.
class Image(models.Model):
    # randomly generated name for the pictures
    name = models.CharField(max_length=100)
    # keyword
    keyword = models.CharField(max_length=100, default='none')
    # add a timestamp
    timestamp = models.DateTimeField(auto_now=True)