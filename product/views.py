from django.shortcuts import render
from rest_framework.decorators import api_view
# Create your views here.
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

@api_view(['GET'])
def get_all_products(request):
    products = Product.objects.all()
    serilizer = ProductSerializer(products, many = True)
    print(products)
    return Response({"products":serilizer.data})
