from django.db import models
from clients.models import Client

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name


class Purchase(models.Model):
    purchase_date = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    

class ProductPurchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)