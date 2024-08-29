from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ProductClass,Category
from .forms import ProductForm ,CategoryForm

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_form.html', {'form': form})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product_confirm_delete.html', {'product': product})


      # ---------crud Catefgory-----------------



def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {'form': form})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category_form.html', {'form': form})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'category_confirm_delete.html', {'category': category})



#  ------------home page-------------------


def home_view(request):
    categories = Category.objects.all()  # Retrieve all categories
    products = Product.objects.all()  # Get all products for the home page
    return render(request, 'home.html', {'products': products, 'categories': categories})

def category_view(request):
    categories = Category.objects.all()  # Get all categories for the sidebar menu
    return render(request, 'category_list.html', {'categories': categories})

def products_by_category_view(request, category_id):
    categories = Category.objects.all()
    category = get_object_or_404(Category, id=category_id)  # Get the specific category
    products = Product.objects.filter(category=category)  # Get products in that category
    return render(request, 'home.html', {'products': products, 'selected_category': category, 'categories': categories})