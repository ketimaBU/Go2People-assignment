from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from main.models import Product


class ProductsListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "products.html"

