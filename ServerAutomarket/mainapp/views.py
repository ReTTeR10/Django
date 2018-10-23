from django.shortcuts import render
from django.template.loader import get_template, render_to_string
from django.http import HttpResponse


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

def list(request):
    #return render(request, 'mainapp/index.html')
    template = get_template('mainapp/list.html')
    content = {
        'title': 'Каталог',
    }
    response_string = template.render(content)

    return HttpResponse(response_string)
