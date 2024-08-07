from django.db import models

class ProductClass(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name    

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, default=None)
    product_class = models.ForeignKey(ProductClass, on_delete=models.CASCADE, null=True, default=None)  # Added

    def __str__(self):
        return self.name
