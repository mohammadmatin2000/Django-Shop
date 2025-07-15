from django.contrib.auth.mixins import LoginRequiredMixin
from .permission import HasCustomerPermission
from django.views.generic import TemplateView
# ======================================================================================================================
class OrderCheckOutView(HasCustomerPermission,LoginRequiredMixin,TemplateView):
    template_name = 'order/checkout.html'
# ======================================================================================================================