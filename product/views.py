from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
# Create your views here.
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from .filters import ProductsFilter
from rest_framework.pagination import PageNumberPagination

@api_view(['GET'])
def get_all_products(request):

    filterset = ProductsFilter(request.GET,queryset = Product.objects.all().order_by('id'))
    count = filterset.qs.count()
    paginator = PageNumberPagination()
    paginator.page_size = 2

    queryset = paginator.paginate_queryset(filterset.qs, request)
    serializer = ProductSerializer(queryset, many = True)
    return Response({"products":serializer.data,"per page":2,"count":count})

@api_view(['GET'])
def get_by_id_product(request,pk):
    product = get_object_or_404(Product,id = pk)
    serializer = ProductSerializer(product,many = False)
    print(product)
    return Response({'product':serializer.data})






    #products = Product.objects.all()
    #serilizer = ProductSerializer(products, many = True)
    #print(products)