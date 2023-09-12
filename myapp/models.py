from django.db import models
from django.utils import timezone

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=255, default="Default Name")
    photo = models.ImageField(upload_to='myimage')
    date = models.DateField(auto_now_add=True)