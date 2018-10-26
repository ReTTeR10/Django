from django.shortcuts import render
from django.template.loader import get_template, render_to_string
from django.http import HttpResponse
import json


def mainapp(request):
    #return render(request, 'mainapp/index.html')
    template = get_template('mainapp/index.html')
    content = {
        'title': 'Каталог',
    }
    response_string = template.render(content)

    return HttpResponse(response_string)


def contacts(request):
    template = get_template('mainapp/contacts.html')
    content = {
        'title': 'Contacts',
    }
    response_string = template.render(content)

    return HttpResponse(response_string)


def catalog(request):
    return render(request, 'mainapp/Catalog.html')


def loginpage(request):
    return render(request, 'mainapp/LoginPage.html')
# Create your views here.


# def list(request):
#     context = {}
#     #return render(request, 'mainapp/index.html')
#     template = get_template('mainapp/list.html')
#     content = {
#         'title': 'Каталог',
#     }
#     response_string = template.render(content)
#
#     with open('D:\Projects\djangoProject\ServerAutomarket\mainapp\data\products.json', 'r') as file:
#         context = json.load(file)
#
#     return render(
#     #return HttpResponse(response_string), render(
#         request, 'D:\Projects\djangoProject\ServerAutomarket\mainapp\\templates\mainapp\list.html',
#         context
#     )
#
#
# def detail(request, idx):
#     context = {}
#     with open('D:\Projects\djangoProject\ServerAutomarket\mainapp\data\products.json', 'r') as file:
#         context = json.load(file)
#
#     return render(
#         request,
#         'D:\Projects\djangoProject\ServerAutomarket\mainapp\\templates\mainapp\detail.html',
#         {
#             'object': context['products'][idx]
#         }
#     )
