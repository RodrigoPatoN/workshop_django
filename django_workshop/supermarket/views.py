from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def get_all_products(request):
    products = Product.objects.all()
    products_serialized = ProductSerializer(products, many=True)
    return Response(products_serialized.data)


@api_view(["GET"])
def get_products_stock(request):
    products = Product.objects.filter(stock__gt=50)
    products_serialized = ProductSerializer(products, many=True)
    return Response(products_serialized.data)


@api_view(["GET"])
def get_products_stock_value(request, value):
    products = Product.objects.filter(stock__gt=value)
    products_serialized = ProductSerializer(products, many=True)
    return Response(products_serialized.data)


@api_view(['POST'])
def add_product(request):
    product = ProductSerializer(data=request.data)
    if product.is_valid():
        product.save()
        return Response(product.data)
    return Response(product.errors)