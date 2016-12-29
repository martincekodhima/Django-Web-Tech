from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    # randomly generated name for the pictures
    title = models.CharField(max_length=100)
    # keyword 1
    keyword1 = models.CharField(max_length=50, default='none')
    # keyword 2
    keyword2 = models.CharField(max_length=50, default='none')
    # keyword 3
    keyword3 = models.CharField(max_length=50, default='none')
    # add a user
    user = models.ForeignKey(User, default=0)
    # add a timestamp
    timestamp = models.DateTimeField(auto_now=True)
    # add the photo
    photo = models.ImageField(upload_to='images', blank=False, default=None)