from django.shortcuts import render
from .models import Product, Category

def index(request):
    return render(request, 'index.html')

def woman(request):
    products_women = Product.objects.filter(category__name='Women')
    return render(request, 'woman.html', {'products': products_women})

def man(request):
    products_men = Product.objects.filter(category__name='Men')
    return render(request, 'men.html', {'products': products_men})



def product_detail(request, id):
    product = Product.objects.filter(Product, id=id)
    context = {'product': product}
    return render(request, 'checkShoe.html', context)

def children(request):
    products_children = Product.objects.filter(category__name='Children')
    return render(request, 'children.html', {'products': products_children})



