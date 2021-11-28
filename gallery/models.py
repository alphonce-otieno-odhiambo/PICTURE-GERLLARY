from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Picture(models.Model):
    image_name = models.CharField(max_length=30)
    image_description = models.CharField(max_length=200)
    image = models.ImageField(upload_to = "images/")
    

    def __str__(self):
        return self.image_name


class Cartegories(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

