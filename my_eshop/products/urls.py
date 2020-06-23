from django.urls import path

from .views import ProductsList,product_detail

urlpatterns = [
    path('products', ProductsList.as_view()),
    path('products-det', product_detail),
]
