from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import ProductModels,ProductStatusModels
# ======================================================================================================================
class ProductsGridView(ListView):
    template_name = "shop/product-grid.html"
    queryset = ProductModels.objects.filter(status=ProductStatusModels.publish.value)
# ======================================================================================================================