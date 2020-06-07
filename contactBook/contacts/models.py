from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length = 200)
    def __str__(self):
        return self.name
    

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length = 100)
    middle_name =models.CharField(max_length = 100, blank=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    image = models.ImageField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name
