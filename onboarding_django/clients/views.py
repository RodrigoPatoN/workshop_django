from django.shortcuts import render
from .models import Client
from rest_framework.response import Response
from .serializers import ClientSerializer
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def get_all_clients(request):
    clients = Client.objects.all()
    serialized_clients = ClientSerializer(clients, many=True)
    return Response(serialized_clients.data)

