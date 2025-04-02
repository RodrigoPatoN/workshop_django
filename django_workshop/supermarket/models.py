from django.db import models
from clients.models import Client

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()

    def __str__(self):
        return self.name


class Purchase(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)


class ProductPurchase(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()