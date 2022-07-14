from django.shortcuts import render
from .serializers import ProductSerializer
from rest_framework import generics, mixins
from .models import Product

class ProductListAPI(generics.ListAPIView, mixins.ListModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)