from django.db import models
import os

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

# Create your models here.
class Quote(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=50)
    image_object = models.ImageField(upload_to="images/", default="")

    def __str__(self):
        return str(self.quote)