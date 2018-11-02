from django.urls import path
from mainapp.views import (
    mainapp, contacts, catalog, loginpage, #list, detail
)


app_name = 'mainapp'


urlpatterns = [
    path('', mainapp, name='mainapp'),
    path('contacts/', contacts, name='contacts'),
    path('Catalog/', catalog, name='Catalog'),
    path('LoginPage/', loginpage, name='LoginPage'),
    path('index/', mainapp, name='mainapp'),
    # path('list/', list),
    # path('<int:idx>', detail),
]
