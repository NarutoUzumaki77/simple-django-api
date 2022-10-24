from django.http import JsonResponse
from django.forms.models import model_to_dict
from .models import Product

from rest_framework.decorators import api_view
from rest_framework.response import Response


def hello_api(request, *args, **kwargs):
    return JsonResponse({"message": "Welcome to Django Api basics."})


def products(request):
    products = Product.objects.all()
    format_data = [product.json() for product in products]
    return JsonResponse({"data": format_data})


def product(request, pk):
    product = Product.objects.get(pk=pk)
    return JsonResponse(model_to_dict(product, fields=["id", "title"]))


@api_view(["GET"])
def api_products(request):
    # Without Serializer
    products = Product.objects.all()
    format_data = [product.json() for product in products]
    return Response(format_data)
