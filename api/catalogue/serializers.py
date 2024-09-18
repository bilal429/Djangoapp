from rest_framework import serializers
from catalog.models import Product, Category, ProductClass

          # Serializer for ProductClass
class ProductClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductClass
        fields = ['id', 'name']

          # Serializer for Category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

           # Serializer for Product
class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    product_class = ProductClassSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'image', 'category', 'product_class']
