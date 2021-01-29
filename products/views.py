from django.shortcuts import render, redirect
from products.models import Product
from products.forms import ProductForm

def create_product(request):
    context = {}
    if request.method == 'POST':
        product = ProductForm(request.POST)
        if product.is_valid():
            product.save()
            return redirect('user:home')
        else:
            print(product.errors)
            context['form'] = product
    return render(request, 'products/create_edit_product.html', context)

def edit_product(request, id):
    product = Product.objects.get(id=id)
    context = { 'product': product, 'action': 'Editar' }
    print('POST:', request.POST)
    if request.method == 'POST':
        product = ProductForm(request.POST, instance=product)
        if product.is_valid():
            product.save()
            return redirect('user:home')
        else:
            print(product.errors)
            context['form'] = product
    return render(request, 'products/create_edit_product.html', context)

def delete_product(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('user:home')