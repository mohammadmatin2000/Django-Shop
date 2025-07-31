from django.views.generic import (
    TemplateView,
    UpdateView,
    DeleteView,
    CreateView,
    ListView,
    DetailView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.shortcuts import redirect
from ..permission import HasCustomerPermission
from .forms import (
    CustomerChangeProfileForm,
    CustomerPasswordChangeForm,
    CustomUserAddressForm,
)
from django.core.exceptions import FieldError
from order.models import UserAddressModel, OrderModels
from shop.models import WishListModels


# ======================================================================================================================
class CustomerDashboardHomeView(
    LoginRequiredMixin, HasCustomerPermission, TemplateView
):
    template_name = "dashboard/customer/home.html"


# ======================================================================================================================
class CustomerSecurityDashboardView(
    LoginRequiredMixin,
    HasCustomerPermission,
    SuccessMessageMixin,
    TemplateView,
    PasswordChangeView,
):
    template_name = "dashboard/customer/profile/security.html"
    form_class = CustomerPasswordChangeForm
    success_url = reverse_lazy("dashboard:customer:security")
    success_message = "رمز با موفقیت تغییر کرد"


# ======================================================================================================================
class CustomerProfileDashboardView(
    LoginRequiredMixin, HasCustomerPermission, SuccessMessageMixin, UpdateView
):
    template_name = "dashboard/customer/profile/profile.html"
    form_class = CustomerChangeProfileForm
    success_url = reverse_lazy("dashboard:customer:profile")
    success_message = "اطلاعات با موفقیت تغییر کرد"

    def get_object(self, queryset=None):
        return self.request.user.user_profile


# ======================================================================================================================
class CustomerProfileImageDashboardView(
    LoginRequiredMixin, HasCustomerPermission, SuccessMessageMixin, UpdateView
):
    http_method_names = ["post"]
    template_name = "dashboard/customer/profile/profile.html"
    success_url = reverse_lazy("dashboard:customer:profile")
    success_message = "عکس با موفقیت تغییر کرد"

    def get_object(self, queryset=None):
        return self.request.user.user_profile

    def form_valid(self, form):
        messages.error("آپلود عکس به مشکل خورده لطفا دوباره تلاش کنید")
        return redirect(reverse_lazy(self.success_url))


# ======================================================================================================================
class CustomerAddressListView(
        LoginRequiredMixin,
        HasCustomerPermission,
        ListView):
    template_name = "dashboard/customer/address/address-list.html"

    def get_queryset(self):
        queryset = UserAddressModel.objects.filter(user=self.request.user)
        if order_by := self.request.GET.get("order_by"):
            try:
                queryset = queryset.order_by(order_by)
            except FieldError:
                pass
        return queryset


# ======================================================================================================================
class CustomerAddressCreateView(
    LoginRequiredMixin, HasCustomerPermission, SuccessMessageMixin, CreateView
):
    template_name = "dashboard/customer/address/address-create.html"

    form_class = CustomUserAddressForm
    success_message = "ایجاد آدرس با موفقیت انجام شد"

    def get_queryset(self):
        return UserAddressModel.objects.filter(user=self.request.user)

    def form_valid(self, form):
        form.instance.user = self.request.user
        super().form_valid(form)
        return redirect(
            reverse_lazy(
                "dashboard:customer:address-edit",
                kwargs={
                    "pk": form.instance.pk}))

    def get_success_url(self):
        return reverse_lazy("dashboard:customer:address-list")


# ======================================================================================================================
class CustomerAddressEditView(
    LoginRequiredMixin, HasCustomerPermission, SuccessMessageMixin, UpdateView
):
    template_name = "dashboard/customer/address/address-edit.html"

    form_class = CustomUserAddressForm
    success_message = "ویرایش آدرس با موفقیت انجام شد"

    def get_queryset(self):
        return UserAddressModel.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse_lazy(
            "dashboard:customer:address-edit",
            kwargs={
                "pk": self.get_object().pk})


# ======================================================================================================================
class CustomerAddressDeleteView(
    LoginRequiredMixin, HasCustomerPermission, SuccessMessageMixin, DeleteView
):
    template_name = "dashboard/customer/address/address-delete.html"

    success_url = reverse_lazy("dashboard:customer:address-list")
    success_message = "حذف آدرس با موفقیت انجام شد"

    def get_queryset(self):
        return UserAddressModel.objects.filter(user=self.request.user)


# ======================================================================================================================
class CustomerOrdersListView(
        LoginRequiredMixin,
        HasCustomerPermission,
        ListView):
    template_name = "dashboard/customer/orders/order-list.html"
    context_object_name = "object_list"
    paginate_by = 10

    def get_paginate_by(self, queryset):
        page_size = self.request.GET.get("page_size", 10)
        try:
            return int(page_size)
        except (TypeError, ValueError):
            return 10

    def get_queryset(self):

        queryset = OrderModels.objects.filter(
            user=self.request.user).prefetch_related("items")
        search = self.request.GET.get("q")
        if search:
            queryset = queryset.filter(title__icontains=search)
        order_by = self.request.GET.get("order_by")
        try:
            if order_by:
                queryset = queryset.order_by(order_by)
        except FieldError:
            pass
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_items"] = self.get_queryset().count()
        return context


# ======================================================================================================================
class CustomerOrdersDeleteView(
    LoginRequiredMixin, HasCustomerPermission, SuccessMessageMixin, DeleteView
):
    model = OrderModels
    template_name = "dashboard/customer/orders/order-delete.html"
    success_url = reverse_lazy("dashboard:customer:orders-list")
    success_message = "سفارش با موفقیت حذف شد."

    def get_queryset(self):
        return OrderModels.objects.filter(user=self.request.user)


# ======================================================================================================================
class CustomerOrdersDetailView(
        LoginRequiredMixin,
        HasCustomerPermission,
        DetailView):
    template_name = "dashboard/customer/orders/order-detail.html"
    context_object_name = "object"

    def get_queryset(self):
        return OrderModels.objects.filter(user=self.request.user)


# ======================================================================================================================
class CustomerOrdersInvoiceView(
        LoginRequiredMixin,
        HasCustomerPermission,
        DetailView):
    template_name = "dashboard/customer/orders/invoice.html"
    context_object_name = "object"

    def get_queryset(self):
        return OrderModels.objects.all()


# ======================================================================================================================
class CustomerWishListView(
        LoginRequiredMixin,
        HasCustomerPermission,
        ListView):
    template_name = "dashboard/customer/wishlist/wishlist.html"

    paginate_by = 10

    def get_paginate_by(self, queryset):
        page_size = self.request.GET.get("page_size", 10)
        try:
            return int(page_size)
        except (TypeError, ValueError):
            return 10

    def get_queryset(self):

        queryset = WishListModels.objects.filter(user=self.request.user)
        search = self.request.GET.get("q")
        if search:
            queryset = queryset.filter(title__icontains=search)
        order_by = self.request.GET.get("order_by")
        category_id = self.request.GET.get("category_id")
        if category_id:
            queryset = queryset.filter(category__id=category_id)
        try:
            if order_by:
                queryset = queryset.order_by(order_by)
        except FieldError:
            pass
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_items"] = self.get_queryset().count()
        return context


# ======================================================================================================================
class CustomerWishListDeleteView(
        LoginRequiredMixin,
        HasCustomerPermission,
        DeleteView):
    http_method_names = ["post"]
    success_url = reverse_lazy("dashboard:customer:wishlist")
    success_message = "محصول با موفقیت از لیست حذف شد"

    def get_queryset(self):
        return WishListModels.objects.filter(user=self.request.user)


# ======================================================================================================================
