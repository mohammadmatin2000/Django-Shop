from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import ProductView,ProductStatusView
# ======================================================================================================================
class ProductsGridView(ListView):
    template_name = "shop/product-grid.html"
    queryset = ProductView.objects.filter(status=ProductStatusView.publish.value)
# ======================================================================================================================