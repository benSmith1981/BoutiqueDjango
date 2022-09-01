from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.

def all_products(request):

    """ A view to show all products and search and sort queries """
    products = Product.objects.all()
    print(products.count)
    context = {
        'products' : products,
    }
    return render(request, 'products/products.html', context)

def product_detail(request, product_id):

    """ A view to show product details """
    products = get_object_or_404(Product, pk=product_id)
   
    context = {
        'products' : products,
    }
    return render(request, 'products/product_detail.html', context)