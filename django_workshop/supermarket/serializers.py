from rest_framework import serializers
from .models import Product, Purchase, ProductPurchase

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    
class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'


class ProductPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPurchase
        fields = '__all__'