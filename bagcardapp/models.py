from django.db import models

class Bag(models.Model):
    name=models.CharField(max_length=200)
    color=models.CharField(max_length=250)
    image=models.ImageField(upload_to='bag_images/')

    def __str__(self):
        return self.name


