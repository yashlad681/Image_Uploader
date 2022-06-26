from django.db import models
from django.utils import timezone
# Create your models here.

class Image(models.Model):
    photo = models.ImageField(upload_to='myimage')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.photo.url.split('/')[-1]
    
   

    
