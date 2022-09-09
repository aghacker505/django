from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

class Product(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=100)
    image = models.ImageField()
    price = models.CharField(max_length=100)
    discount = models.CharField(max_length=50)
    unique_id = models.CharField(max_length=100)

    def __str__(self):
        return self.name