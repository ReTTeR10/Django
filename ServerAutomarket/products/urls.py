from django.urls import path
from .views import (
    product_list, product_detail
)

app_name = 'products'

urlpatterns = [
    path('list/', product_list, name='list'),
    path('<int:idx>/', product_detail, name='detail'),
]
