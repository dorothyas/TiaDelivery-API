from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Items
from .serializers import ItemsSerializer

class ItemsViewSet(viewsets.ModelViewSet):
  # permission_classes = [IsAuthenticated]
    serializer_class = ItemsSerializer
    queryset = Items.objects.all()
