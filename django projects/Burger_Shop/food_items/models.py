from django.db import models
from datetime import datetime

# Create your models here.
class Food(models.Model):
    food_name = models.CharField(max_length=200)
    catagory = models.CharField(max_length=200, default='')
    description = models.TextField(blank=True)
    price = models.IntegerField()
    
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.food_name