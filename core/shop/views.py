from django.core.paginator import EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import ProductModels, ProductStatusModels
# ======================================================================================================================
class ProductsGridView(ListView):
    template_name = "shop/product-grid.html"
    queryset = ProductModels.objects.filter(status=ProductStatusModels.publish.value)
    paginate_by = 9
# ======================================================================================================================
class ProductsDetailView(DetailView):
    template_name = "shop/product-detail.html"
    queryset = ProductModels.objects.filter(status=ProductStatusModels.publish.value)
# ======================================================================================================================