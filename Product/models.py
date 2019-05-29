from django.db import models
from User.models import User
# Create your models here.
class Product(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 200)
    type = models.CharField(max_length = 200)
    stock = models.IntegerField()
    purpose = models.CharField(max_length = 100)
    price = models.FloatField()
    description = models.CharField(max_length = 500)

class IncludedProducts(models.Model):

    id = models.AutoField(primary_key=True)
    product = models.ManyToManyField(Product)
    quantity = models.IntegerField()

class Bill(models.Model):

    id = models.AutoField(primary_key=True)
    datetime = models.DateTimeField()
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    total = models.FloatField()

class ProductBill(models.Model):

    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    bill = models.ForeignKey(Bill,on_delete = models.CASCADE)
    quantity = models.IntegerField()
    cost = models.FloatField()
    reference = models.CharField(max_length =  200)
