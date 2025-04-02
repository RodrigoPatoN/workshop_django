from django.shortcuts import render
from .models import Product, Purchase
from .serializers import ProductSerializer, PurchaseSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def get_all_products(request):
    products = Product.objects.all()
    serialized_products = ProductSerializer(products, many=True)
    return Response(serialized_products.data)


@api_view(['GET'])
def get_products_price(request):
    products = Product.objects.filter(price__gt=50)
    serialized_products = ProductSerializer(products, many=True)
    return Response(serialized_products.data)


@api_view(['GET'])
def get_products_stock(request):
    products = Product.objects.filter(quantity__gt=0)
    serialized_products = ProductSerializer(products, many=True)
    return Response(serialized_products.data)


@api_view(['GET'])
def get_product_price_user(request, price):
    products = Product.objects.filter(price__gt=price)
    serialized_products = ProductSerializer(products, many=True)
    return Response(serialized_products.data)


@api_view(['GET'])
def get_product_stock_user(request, stock):
    products = Product.objects.filter(quantity__gt=stock)
    serialized_products = ProductSerializer(products, many=True)
    return Response(serialized_products.data)


@api_view(['GET'])
# get info purchase
def get_purchase(request, id):
    purchases = Purchase.objects.get(id=id)
    serialized_purchases = PurchaseSerializer(purchases, many=True)
    return Response(serialized_purchases.data)


@api_view(['POST'])
def add_product(request):
    product = ProductSerializer(data=request.data)
    if product.is_valid():
        product.save()
        return Response(product.data)
    return Response(product.errors)