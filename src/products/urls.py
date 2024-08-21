from django.urls import path
from .views import product_list, create_multiple_products

urlpatterns = [
    path('', product_list, name="product_list"),
    path('add', create_multiple_products, name="create_product")
]
