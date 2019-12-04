from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
import django_filters

from main.models import Product


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Product
        fields = {
            'price': ['lt', 'gt', 'lte', 'gte'],
            'expiration_date': ['exact', 'year__gt'],
        }


class ProductsListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "products.html"

    def get_queryset(self):
        qs = self.model.objects.all()
        product_filtered_list = ProductFilter(self.request.GET, queryset=qs)
        return product_filtered_list.qs
