from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Category, Product




def popular_list(request):
    products = Product.objects.filter(available=True).order_by('?')
    return render(request, 
                  'main/index/index.html', 
                  {'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product,
                                slug=slug,
                                available=True)
    
    
    return render(request,
                  'main/product/detail.html',
                   {'product': product})
    