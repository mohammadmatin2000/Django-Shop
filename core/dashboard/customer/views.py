from django.views.generic import TemplateView,UpdateView,DeleteView,CreateView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from ..permission import HasCustomerPermission
from .forms import CustomerChangeProfileForm,CustomerPasswordChangeForm,CustomUserAddressForm
from django.core.exceptions import FieldError
from order.models import UserAddressModel
# ======================================================================================================================
class CustomerDashboardHomeView(LoginRequiredMixin,HasCustomerPermission,TemplateView):
    template_name = "dashboard/customer/home.html"
# ======================================================================================================================
class CustomerSecurityDashboardView(LoginRequiredMixin,HasCustomerPermission,SuccessMessageMixin,TemplateView,PasswordChangeView):
    template_name = "dashboard/customer/profile/security.html"
    form_class = CustomerPasswordChangeForm
    success_url = reverse_lazy("dashboard:customer:security")
    success_message = "رمز با موفقیت تغییر کرد"
# ======================================================================================================================
class CustomerProfileDashboardView(LoginRequiredMixin,HasCustomerPermission,SuccessMessageMixin,UpdateView):
    template_name = "dashboard/customer/profile/profile.html"
    form_class = CustomerChangeProfileForm
    success_url = reverse_lazy("dashboard:customer:profile")
    success_message = "اطلاعات با موفقیت تغییر کرد"
    def get_object(self, queryset=None):
        return self.request.user.user_profile
# ======================================================================================================================
class CustomerProfileImageDashboardView(LoginRequiredMixin,HasCustomerPermission,SuccessMessageMixin,UpdateView):
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
class CustomerAddressListView(LoginRequiredMixin, HasCustomerPermission, ListView):
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
class CustomerAddressCreateView(LoginRequiredMixin, HasCustomerPermission, SuccessMessageMixin, CreateView):
    template_name = "dashboard/customer/address/address-create.html"

    form_class = CustomUserAddressForm
    success_message = "ایجاد آدرس با موفقیت انجام شد"

    def get_queryset(self):
        return UserAddressModel.objects.filter(user=self.request.user)

    def form_valid(self, form):
        form.instance.user = self.request.user
        super().form_valid(form)
        return redirect(reverse_lazy("dashboard:customer:address-edit", kwargs={"pk": form.instance.pk}))

    def get_success_url(self):
        return reverse_lazy("dashboard:customer:address-list")
# ======================================================================================================================
class CustomerAddressEditView(LoginRequiredMixin, HasCustomerPermission, SuccessMessageMixin, UpdateView):
    template_name = "dashboard/customer/address/address-edit.html"

    form_class = CustomUserAddressForm
    success_message = "ویرایش آدرس با موفقیت انجام شد"

    def get_queryset(self):
        return UserAddressModel.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse_lazy("dashboard:customer:address-edit", kwargs={"pk": self.get_object().pk})
# ======================================================================================================================
class CustomerAddressDeleteView(LoginRequiredMixin, HasCustomerPermission, SuccessMessageMixin, DeleteView):
    template_name = "dashboard/customer/address/address-delete.html"

    success_url = reverse_lazy("dashboard:customer:address-list")
    success_message = "حذف آدرس با موفقیت انجام شد"

    def get_queryset(self):
        return UserAddressModel.objects.filter(user=self.request.user)
# ======================================================================================================================