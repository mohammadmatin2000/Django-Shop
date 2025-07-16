from django.contrib.auth.mixins import LoginRequiredMixin
from .permission import HasCustomerPermission
from django.views.generic import TemplateView
from .models import UserAddressModel
# ======================================================================================================================
class OrderCheckOutView(HasCustomerPermission,LoginRequiredMixin,TemplateView):
    template_name = 'order/checkout.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['addresses'] = UserAddressModel.objects.filter(user=self.request.user)
        return context
# ======================================================================================================================