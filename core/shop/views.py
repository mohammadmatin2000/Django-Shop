from django.shortcuts import render
from django.views.generic import TemplateView
# ======================================================================================================================
class ProductsGridView(TemplateView):
    template_name = "shop/product-grid.html"
# ======================================================================================================================