from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from ..permission import HasAdminPermission
from .forms import PasswordChangeForm
# ======================================================================================================================
class AdminDashboardHomeView(LoginRequiredMixin,HasAdminPermission,TemplateView):
    template_name = "dashboard/admin/home.html"
# ======================================================================================================================
class AdminSecurityView(LoginRequiredMixin,HasAdminPermission,SuccessMessageMixin,TemplateView,PasswordChangeView):
    template_name = "dashboard/admin/profile/security.html"
    form_class = PasswordChangeForm
    success_url = reverse_lazy("dashboard:admin:security")
    success_message = "رمز با موفقیت تغییر کرد"
# ======================================================================================================================