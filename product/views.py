from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
# Create your views here.
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from .filters import ProductsFilter

@api_view(['GET'])
def get_all_products(request):
    #products = Product.objects.all()
    filterset = ProductsFilter(request.GET,queryset = Product.objects.all().order_by('id'))
    #serilizer = ProductSerializer(products, many = True)
    serilizer = ProductSerializer(filterset.qs, many = True)
    #print(products)
    return Response({"products":serilizer.data})

@api_view(['GET'])
def get_by_id_product(request,pk):
    product = get_object_or_404(Product,id = pk)
    serializer = ProductSerializer(product,many = False)
    print(product)
    return Response({'product':serializer.data})


