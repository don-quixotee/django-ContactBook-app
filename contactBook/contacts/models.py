from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length = 200)
    

class people(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length = 100)
    middle_name =models.CharField(max_length = 100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    image = models.ImageField()
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
