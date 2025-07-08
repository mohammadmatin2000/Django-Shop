from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..permission import HasCustomerPermission
# ======================================================================================================================
class CustomerDashboardHomeView(LoginRequiredMixin,HasCustomerPermission,TemplateView):
    template_name = "dashboard/customer/home.html"
# ======================================================================================================================