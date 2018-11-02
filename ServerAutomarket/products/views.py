from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.template.loader import get_template, render_to_string
from django.http import HttpResponse
from django.core.paginator import Paginator
import json
from django.urls import reverse_lazy
from django.http import Http404

from .forms import ProductForm
from .models import Product

from .models import Product


def product_delete(request, pk):
    obj = get_object_or_404(Product, pk=pk)
    success_url = reverse_lazy('mainapp:index')

    if request.method == 'POST':
        obj.delete()

        return redirect(success_url)

    return render(request, 'products/delete.html', {'obj': obj})


def product_update(request, pk):
    # try:
    #     obj = Product.objects.get(pk=pk)
    # except Exception as err:
    #     raise Http404
    obj = get_object_or_404(Product, pk=pk)
    form = ProductForm(instance=obj)
    success_url = reverse_lazy('mainapp:index')

    if request.method == 'POST':
        form = ProductForm(
            request.POST,
            files=request.FILES,
            instance=obj
        )

        if form.is_valid():
            form.save()

            return redirect(success_url)

    return render(
        request,
        'products/update.html',
        {
            'form': form,
            'obj': obj
        }
    )


def product_create(request):
    form = ProductForm()
    success_url = reverse_lazy('mainapp:index')

    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect(success_url)

    return render(request, 'products/create.html', {'form': form})


def product_list(request):
    context = {}
    #return render(request, 'mainapp/index.html')
    template = get_template('D:\Projects\djangoProject\ServerAutomarket\products\\templates\products\list.html')
    content = {
       'title': 'Каталог',
    }
    response_string = template.render(content)

    # with open('products/data/products.json', 'r') as file:
    #     context = json.load(file)
    #
    # return render(
    # #HttpResponse(response_string), render(
    #     request, 'products/list.html',
    #     context
    # )

    # query = Product.objects.all()

    query = get_list_or_404(Product)
    page = request.GET.get('page')
    paginator = Paginator(query, 10)

    products = paginator.get_page(page)

    return render(request, 'products/list.html', {'products': products})
    # return render(request, 'products/list.html', {'products': query})



def product_detail(request, pk):
    context = {}
    # with open('products/data/products.json', 'r') as file:
    #     context = json.load(file)

    template = get_template('D:\Projects\djangoProject\ServerAutomarket\products\\templates\products\detail.html')
    content = {
        'title': 'sad',
    }
    response_string = template.render(content)

    # return render(
    #     request,
    #     'products/detail.html',
    #     {
    #         'object': context['products'][idx]
    #     }
    # )
    obj = get_object_or_404(Product, pk=pk)

    return render(request, 'products/detail.html', {'object': obj})

    # obj = Product.objects.get(id=pk)
    # return render(request, 'products/detail.html', {'object': obj})