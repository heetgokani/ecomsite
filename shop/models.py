from django.db import models

# Create your models here.
class Products(models.Model):
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    discounted_price=models.IntegerField()
    description=models.TextField()
    rating=models.FloatField()
    image=models.CharField(max_length=300)
    stock=models.IntegerField()

    def __str__(self):
        return self.name

class Order(models.Model):
    
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    email =models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    total = models.CharField(max_length=200)
    def __str__(self):
        return self.name