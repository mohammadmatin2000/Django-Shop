from django.views.generic import ListView, DetailView,View
from django.core.exceptions import FieldError
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ProductModels, ProductStatusModels, ProductCategoryModels,WishListModels
# ======================================================================================================================
class ProductsGridView(ListView):
    template_name = "shop/product-grid.html"
    paginate_by = 10

    def get_paginate_by(self, queryset):

        page_size = self.request.GET.get("page_size",9)
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

        min_price = self.request.GET.get("min_price")
        if min_price:
            queryset = queryset.filter(price__gte=min_price)

        max_price = self.request.GET.get("max_price")
        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        order_by = self.request.GET.get("order_by")
        try:
            if order_by:
                queryset = queryset.order_by(order_by)
        except FieldError:
            pass
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategoryModels.objects.all()
        context["wishlist_items"] = WishListModels.objects.filter(user=self.request.user).values_list(
            "product__id", flat=True) if self.request.user.is_authenticated else []
        context["total_items"] = self.get_queryset().count()

        return context
# ======================================================================================================================
class ProductsDetailView(DetailView):
    template_name = "shop/product-detail.html"
    queryset = ProductModels.objects.filter(status=ProductStatusModels.publish.value)
# ======================================================================================================================
class AddToWishlistView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id')

        try:
            product = ProductModels.objects.get(id=product_id)
        except ProductModels.DoesNotExist:
            return JsonResponse({"error": "محصول یافت نشد."}, status=404)

        wishlist_item = WishListModels.objects.filter(user=request.user, product=product).first()

        if wishlist_item:
            wishlist_item.delete()
            message = "از لیست علاقه‌مندی‌ها حذف شد."
            in_wishlist = False
        else:
            WishListModels.objects.create(user=request.user, product=product)
            message = "به لیست علاقه‌مندی‌ها اضافه شد."
            in_wishlist = True

        return JsonResponse({"message": message, "in_wishlist": in_wishlist})

    def get(self, request, *args, **kwargs):
        return JsonResponse({"error": "درخواست نامعتبر."}, status=400)

# ======================================================================================================================