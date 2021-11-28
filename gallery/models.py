from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Picture(models.Model):
    image_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to = "images/")
    

    def __str__(self):
        return self.image_name

