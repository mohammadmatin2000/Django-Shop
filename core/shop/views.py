from django.core.paginator import EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import ProductModels, ProductStatusModels, ProductCategoryModels
# ======================================================================================================================
class ProductsGridView(ListView):
    template_name = "shop/product-grid.html"
    paginate_by = 9

    def get_paginate_by(self, queryset):
        page_size = self.request.GET.get("page_size")
        if page_size:
            try:
                return int(page_size)
            except ValueError:
                pass
        return page_size

    def get_queryset(self):
        queryset = ProductModels.objects.filter(status=ProductStatusModels.publish.value)
        search = self.request.GET.get("q")
        if search:
            queryset = queryset.filter(title__icontains=search)
        category_id = self.request.GET.get("category_id")
        if category_id:
            queryset = queryset.filter(category__id=category_id)
        order_by = self.request.GET.get("order_by")
        if order_by:
            queryset = queryset.order_by(order_by)
        return queryset
    def get_context_data(self, **kwargs):
        categories = ProductCategoryModels.objects.all()
        context = super(ProductsGridView, self).get_context_data(**kwargs)
        context['categories'] = categories
        return context
# ======================================================================================================================
class ProductsDetailView(DetailView):
    template_name = "shop/product-detail.html"
    queryset = ProductModels.objects.filter(status=ProductStatusModels.publish.value)
# ======================================================================================================================
