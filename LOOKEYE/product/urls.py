
from django.contrib import admin
from django.urls import path
from product.views import ProductListAPI

urlpatterns = [
    path('api/product', ProductListAPI.as_view()),
]
