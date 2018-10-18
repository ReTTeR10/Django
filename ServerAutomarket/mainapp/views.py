from django.shortcuts import render


def mainapp(request):
    return render(request, 'mainapp/index.html')


def contacts(request):
    return render(request, 'mainapp/contacts.html')


def catalog(request):
    return render(request, 'mainapp/Catalog.html')


def loginpage(request):
    return render(request, 'mainapp/LoginPage.html')
# Create your views here.
