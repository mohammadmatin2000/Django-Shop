from django.views.generic import TemplateView, UpdateView, ListView, DeleteView , CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from ..permission import HasAdminPermission
from .forms import AdminPasswordChangeForm,AdminChangeProfileForm,AdminUpdateProductForm,AdminCouponForm
from order.models import CouponModels
from django.core.exceptions import FieldError
from shop.models import ProductModels, ProductStatusModels, ProductCategoryModels
# ======================================================================================================================
class AdminDashboardHomeView(LoginRequiredMixin,HasAdminPermission,TemplateView):
    template_name = "dashboard/admin/home.html"
# ======================================================================================================================
class AdminSecurityView(LoginRequiredMixin,HasAdminPermission,SuccessMessageMixin,TemplateView,PasswordChangeView):
    template_name = "dashboard/admin/profile/security.html"
    form_class = AdminPasswordChangeForm
    success_url = reverse_lazy("dashboard:admin:security")
    success_message = "رمز با موفقیت تغییر کرد"
# ======================================================================================================================
class AdminProfileView(LoginRequiredMixin,HasAdminPermission,SuccessMessageMixin,UpdateView):
    template_name = "dashboard/admin/profile/profile.html"
    form_class = AdminChangeProfileForm
    success_url = reverse_lazy("dashboard:admin:profile")
    success_message = "اطلاعات با موفقیت تغییر کرد"
    def get_object(self, queryset=None):
        return self.request.user.user_profile
# ======================================================================================================================
class AdminProfileImageView(LoginRequiredMixin,HasAdminPermission,SuccessMessageMixin,UpdateView):
    http_method_names = ["post"]
    template_name = "dashboard/admin/profile/profile.html"
    success_url = reverse_lazy("dashboard:admin:profile")
    success_message = "عکس با موفقیت تغییر کرد"
    def get_object(self, queryset=None):
        return self.request.user.user_profile
    def form_valid(self, form):
        messages.error("آپلود عکس به مشکل خورده لطفا دوباره تلاش کنید")
        return redirect(reverse_lazy(self.success_url))

# ======================================================================================================================
class AdminProductListView(LoginRequiredMixin,HasAdminPermission,SuccessMessageMixin,ListView):
    template_name = "dashboard/admin/product/product-list.html"
    paginate_by = 10

    def get_paginate_by(self, queryset):

        page_size = self.request.GET.get("page_size", 9)
        if page_size:
            try:
                return int(page_size)
            except ValueError:
                pass
        return page_size

    def get_queryset(self):
        queryset = ProductModels.objects.all()
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
        context["total_items"] = self.get_queryset().count()

        return context
# ======================================================================================================================
class AdminProductUpdateView(LoginRequiredMixin,HasAdminPermission,SuccessMessageMixin,UpdateView):
    template_name = "dashboard/admin/product/product-update.html"
    queryset = ProductModels.objects.all()
    success_message = "محصول شما با موفقیت ویرایش شد "
    form_class = AdminUpdateProductForm
    def get_success_url(self):
        return reverse_lazy('dashboard:admin:product-update', kwargs={'pk': self.object.pk})
# ======================================================================================================================
class AdminProductDeleteView(LoginRequiredMixin,HasAdminPermission,SuccessMessageMixin,DeleteView):
    template_name = "dashboard/admin/product/product-delete.html"
    queryset = ProductModels.objects.all()
    success_message = "محصول شما با موفقیت حذف شد"
    success_url = reverse_lazy('dashboard:admin:products-list')
# ======================================================================================================================
class AdminProductCreateView(LoginRequiredMixin,HasAdminPermission,SuccessMessageMixin,CreateView):
    template_name = "dashboard/admin/product/product-create.html"
    queryset = ProductModels.objects.all()
    success_message = "محصول شما با موفقیت ایجاد شد"
    success_url = reverse_lazy('dashboard:admin:products-list')
    form_class = AdminUpdateProductForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# ======================================================================================================================
class AdminCouponsListView(LoginRequiredMixin,HasAdminPermission,SuccessMessageMixin,ListView):
    paginate_by = 10
    model = CouponModels
    template_name = "dashboard/admin/coupon/coupon-list.html"
    context_object_name = "coupons"
    def get_queryset(self):
        qs = CouponModels.objects.all()
        q = self.request.GET.get("q")
        if q:
            qs = qs.filter(code__icontains=q)
        order_by = self.request.GET.get("order_by")
        if order_by:
            qs = qs.order_by(order_by)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_items"] = CouponModels.objects.count()
        return context
# ======================================================================================================================
class AdminCouponCreateView(LoginRequiredMixin,HasAdminPermission,SuccessMessageMixin,CreateView):
    model = CouponModels
    form_class = AdminCouponForm
    template_name = "dashboard/admin/coupon/coupon-create.html"
    success_url = reverse_lazy('dashboard:admin:coupon-list')

    def form_valid(self, form):
        messages.success(self.request, "کد تخفیف با موفقیت ایجاد شد.")
        return super().form_valid(form)
# ======================================================================================================================
class AdminCouponUpdateView(LoginRequiredMixin,HasAdminPermission,SuccessMessageMixin,UpdateView):
    model = CouponModels
    form_class = AdminCouponForm
    template_name = "dashboard/admin/coupon/coupon-update.html"
    success_url = reverse_lazy('dashboard:admin:coupon-list')
    def form_valid(self, form):
        messages.success(self.request, "کد تخفیف با موفقیت ویرایش شد.")
        return super().form_valid(form)
# ======================================================================================================================
class AdminCouponDeleteView(LoginRequiredMixin,HasAdminPermission,SuccessMessageMixin,DeleteView):
    model = CouponModels
    template_name = "dashboard/admin/coupon/coupon-delete.html"
    success_url = reverse_lazy('dashboard:admin:coupon-list')

# ======================================================================================================================