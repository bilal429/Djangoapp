from django.contrib import admin
from .models import Product, ProductClass, Category
from .forms import ProductForm

class ProductClassAdmin(admin.ModelAdmin):
    list_display = ('name',)
    

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    

# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['name','price','category','product_class']


                    # or

class ProductAdmin(admin.ModelAdmin):
    form = ProductForm 
    list_display = ('name', 'price','image', 'category', 'product_class')  


 

admin.site.register(ProductClass, ProductClassAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
