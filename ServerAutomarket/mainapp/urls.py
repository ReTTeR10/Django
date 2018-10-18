from django.urls import path
from mainapp.views import (
    mainapp, contacts, catalog, loginpage
)




urlpatterns = [
    path('', mainapp),
    path('index/', mainapp),
    path('contacts/', contacts),
    path('Catalog/', catalog),
    path('LoginPage/', loginpage),
]
