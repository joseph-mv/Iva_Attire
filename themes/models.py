from django.db import models

# Create your models here.

#model for site
class SiteSetting(models.Model):
    banner=models.ImageField(upload_to='media/site')
    caption=models.TextField()