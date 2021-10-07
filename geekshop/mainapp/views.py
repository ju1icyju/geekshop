from django.shortcuts import render
from mainapp.models import Product, ProductCategory
from django.shortcuts import get_object_or_404


def main(request):
    title = 'Главная'
    products = Product.objects.all()
    content = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', content)

def products(request, pk=None):
    print(pk)

    title = 'продукты'
    links_menu = ProductCategory.objects.all()

    if pk ==0:
        products= Product.objects.all().order_by('price')
        category = {'name': 'все'}
    else:
        category = get_object_or_404(ProductCategory, pk=pk)
        products  = Product.objects.filter(category_pk=pk).order_by('прайс')

    content = {
        'title': title,
        'links_menu': links_menu,
        'category': category,
        'products': products,
    }

    return render(request, 'mainapp/products_list.html', content)

    same_products = Product.objects.all()[3:5]

    content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products
    }

def contact(request):
    return render(request, 'mainapp/contact.html')

def temp(request):
    return render(request, 'mainapp/temp1.html')
