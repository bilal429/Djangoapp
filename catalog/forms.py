from django import forms
from .models import Product,Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'image', 'category','product_class']
        

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']