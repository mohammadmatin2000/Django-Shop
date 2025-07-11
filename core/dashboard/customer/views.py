from django.views.generic import TemplateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from ..permission import HasCustomerPermission
from .forms import CustomerChangeProfileForm,CustomerPasswordChangeForm
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