from django.views.generic import TemplateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from ..permission import HasAdminPermission
from .forms import AdminPasswordChangeForm,AdminChangeProfileForm
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