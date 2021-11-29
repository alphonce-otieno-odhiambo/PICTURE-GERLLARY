from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_Category(self):
        self.save()

    def delete_Category(self):
        self.delete()

    #def __str__(self):
        #  return self.name



class Picture(models.Model):
    image_name = models.CharField(max_length=30)
    category = models.ForeignKey('Category',on_delete=models.CASCADE,null=True)
    image_description = models.CharField(max_length=200)
    image = models.ImageField(upload_to = "media/images/")
    
    
    

    def __str__(self):
        return self.image_name




