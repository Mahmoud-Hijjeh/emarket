import django_filters
from .models import Product

class ProductsFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr = 'iexact') 

    class Meta:
        model = Product
        fields = ['category', 'brand']