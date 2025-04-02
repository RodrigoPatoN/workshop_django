from django.urls import path
from .views import get_all_products, get_products_price, get_products_stock, get_product_price_user, get_product_stock_user, get_purchase, add_product

urlpatterns = [
    path("products/all/", get_all_products),
    path("products/price/", get_products_price),
    path("products/stock/", get_products_stock),
    path("products/price/<int:price>/", get_product_price_user),
    path("products/stock/<int:stock>/", get_product_stock_user),
    path("purchase/<int:id>/", get_purchase),
    path("add_product/", add_product),
] 