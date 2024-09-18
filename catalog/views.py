from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ProductClass,Category
from .forms import ProductForm ,CategoryForm
from cart.models import Cart, CartItem

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

    # Retrieve cart data
    cart_id = request.session.get('cart_id')
    cart_items = CartItem.objects.filter(cart_id=cart_id) if cart_id else []

    context = {
        'products': products,
        'categories': categories,
        'cart_items': cart_items,  # Pass cart items to the template
    }
    return render(request, 'home.html', context)

def category_view(request):
    categories = Category.objects.all()  # Get all categories for the sidebar menu

    # Retrieve cart data
    cart_id = request.session.get('cart_id')
    cart_items = CartItem.objects.filter(cart_id=cart_id) if cart_id else []

    context = {
        'categories': categories,
        'cart_items': cart_items,  # Pass cart items to the template
    }
    return render(request, 'category_list.html', context)

def products_by_category_view(request, category_id):
    categories = Category.objects.all()  # Get all categories for the sidebar
    category = get_object_or_404(Category, id=category_id)  # Get the specific category
    products = Product.objects.filter(category=category)  # Get products in that category

    # Retrieve cart data
    cart_id = request.session.get('cart_id')
    cart_items = CartItem.objects.filter(cart_id=cart_id) if cart_id else []

    context = {
        'products': products,
        'selected_category': category,
        'categories': categories,
        'cart_items': cart_items,  # Pass cart items to the template
    }
    return render(request, 'home.html', context)


# --------------------------product   Detail ------------------------------


def product_detail_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    categories = Category.objects.all()

    # Retrieve cart data
    cart_id = request.session.get('cart_id')
    cart_items = CartItem.objects.filter(cart_id=cart_id) if cart_id else []

    context = {
        'product': product,
        'categories': categories,
        'cart_items': cart_items,
    }
    return render(request, 'product_detail.html', context)