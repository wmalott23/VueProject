from django.db import models

# Create your models here.

class Image(models.Model):
    title = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)