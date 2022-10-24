from django.urls import path

from . import views


urlpatterns = [
    path("", views.hello_api),
    path("products/", views.products),
    path("product/<int:pk>/", views.product),
    path("v1/products/", views.api_products),
]
