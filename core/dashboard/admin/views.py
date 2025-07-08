from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..permission import HasAdminPermission
# ======================================================================================================================
class AdminDashboardHomeView(LoginRequiredMixin,HasAdminPermission,TemplateView):
    template_name = "dashboard/admin/home.html"
# ======================================================================================================================