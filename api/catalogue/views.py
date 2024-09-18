from rest_framework import generics
from catalog.models import Product, Category, ProductClass
from .serializers import ProductSerializer, CategorySerializer, ProductClassSerializer

class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Product Detail View (Retrieve, Update, Delete)
class ProductDetailView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Category Detail View (Retrieve, Update, Delete)
class CategoryDetailView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# ProductClass Detail View (Retrieve, Update, Delete)
class ProductClassDetailView(generics.ListCreateAPIView):
    queryset = ProductClass.objects.all()
    serializer_class = ProductClassSerializer
