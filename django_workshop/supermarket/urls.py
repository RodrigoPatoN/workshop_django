from django.contrib import admin
from django.urls import path
from .views import get_all_products, get_products_stock, get_products_stock_value, add_product

urlpatterns = [
    path("products/all", get_all_products),
    path("products/stock", get_products_stock),
    path("products/stock/<int:value>/", get_products_stock_value),
    path("products/add", add_product),
]
