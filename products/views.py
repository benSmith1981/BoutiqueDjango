from django.shortcuts import render
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