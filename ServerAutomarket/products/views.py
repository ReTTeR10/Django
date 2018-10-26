from django.shortcuts import render
from django.template.loader import get_template, render_to_string
from django.http import HttpResponse
import json

def product_list(request):
    context = {}
    #return render(request, 'mainapp/index.html')
    template = get_template('D:\Projects\djangoProject\ServerAutomarket\products\\templates\products\list.html')
    content = {
       'title': 'Каталог',
    }
    response_string = template.render(content)

    with open('products/data/products.json', 'r') as file:
        context = json.load(file)

    return render(
    #HttpResponse(response_string), render(
        request, 'products/list.html',
        context
    )


def product_detail(request, idx):
    context = {}
    with open('products/data/products.json', 'r') as file:
        context = json.load(file)

    template = get_template('D:\Projects\djangoProject\ServerAutomarket\products\\templates\products\detail.html')
    content = {
        'title': 'sad',
    }
    response_string = template.render(content)

    return render(
        request,
        'products/detail.html',
        {
            'object': context['products'][idx]
        }
    )
