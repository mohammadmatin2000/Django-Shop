from django.contrib.auth.mixins import LoginRequiredMixin
from .permission import HasCustomerPermission
from django.views.generic import FormView
from .models import UserAddressModel
from .forms import OrderCreateForm
from cart.models import CartModels
# ======================================================================================================================
class OrderCheckOutView(HasCustomerPermission,LoginRequiredMixin,FormView):
    template_name = 'order/checkout.html'
    form_class = OrderCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = CartModels.objects.get(user=self.request.user)
        context["addresses"] = UserAddressModel.objects.filter(
            user=self.request.user)
        total_price = cart.calculate_total_price()
        context["total_price"] = total_price
        context["total_tax"] = round((total_price * 9) / 100)
        return context
# ======================================================================================================================