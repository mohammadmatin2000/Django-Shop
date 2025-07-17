from django.contrib.auth.mixins import LoginRequiredMixin
from .permission import HasCustomerPermission
from django.views.generic import FormView, TemplateView, CreateView
from .models import UserAddressModel
from .forms import OrderCreateForm
from cart.models import CartModels
from django.urls import reverse_lazy
# ======================================================================================================================
class OrderCheckOutView(HasCustomerPermission,LoginRequiredMixin,FormView):
    template_name = 'order/checkout.html'
    form_class = OrderCreateForm
    success_url = reverse_lazy('order:complete')

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

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
class OrderCompleteView(HasCustomerPermission,LoginRequiredMixin,TemplateView):
    template_name = 'order/complete.html'

# ======================================================================================================================