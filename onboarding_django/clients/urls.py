from django.urls import path
from .views import get_all_clients

urlpatterns = [
    path("all/", get_all_clients),
]