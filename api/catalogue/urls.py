from django.urls import path
from api.catalogue.views import  ProductDetailView,CategoryDetailView,ProductClassDetailView,ProductListView

urlpatterns = [
    path('productslist/',ProductListView.as_view(),name='productlist'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    # path('product-classes/<int:pk>/', ProductClassDetailView.as_view(), name='productclass-detail'),

]
