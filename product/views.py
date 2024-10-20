from django.shortcuts import render
from rest_framework.decorators import api_view
# Create your views here.
from rest_framework.response import Response
from .models import Product

@api_view(['GET'])
def get_all_products(request):
    products = Product.objects.all()
    print(products)
    return Response({"muhammad":"Essa"})
