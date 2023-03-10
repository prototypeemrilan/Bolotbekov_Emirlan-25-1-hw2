from django.shortcuts import render
from products.models import Product

# Create your views here.

def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')

def products_view(request):
    if request.method == 'GET':
        grade = Product.objects.all()

        context = {
            'products': grade
        }

        return render(request, 'products/products.html', context=context)