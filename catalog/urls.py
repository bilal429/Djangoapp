from django.urls import path
from .views import product_create, product_list, product_update, product_delete,category_list, category_create, category_update, category_delete, home_view,category_view,products_by_category_view

urlpatterns = [

    path('',home_view, name='home'),
    path('categories/', category_view, name='category_list'),
    path('categories/<int:category_id>/',products_by_category_view, name='products_by_category'),

    path('products/', product_list, name='product_list'),
    path('products/create/', product_create, name='product_create'),
    path('products/<int:pk>/update/', product_update, name='product_update'),
    path('products/<int:pk>/delete/', product_delete, name='product_delete'),
    path('categories/', category_list, name='category_list'),
    path('categories/create/', category_create, name='category_create'),
    path('categories/<int:pk>/update/', category_update, name='category_update'),
    path('categories/<int:pk>/delete/', category_delete, name='category_delete'),
]
