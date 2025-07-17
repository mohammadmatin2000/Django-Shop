from django.contrib.auth.mixins import LoginRequiredMixin
from .permission import HasCustomerPermission
from django.views.generic import FormView, TemplateView, CreateView
from .models import UserAddressModel
from .forms import OrderCreateForm
from cart.models import CartModels,CartItemsModels
from .models import OrderModels,OrderItemModels
from django.urls import reverse_lazy
from django.shortcuts import redirect
# ======================================================================================================================
class OrderCheckOutView(HasCustomerPermission,LoginRequiredMixin,FormView):
    template_name = 'order/checkout.html'
    form_class = OrderCreateForm
    success_url = reverse_lazy('order:complete')



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = CartModels.objects.get(user=self.request.user)
        context["addresses"] = UserAddressModel.objects.filter(
            user=self.request.user)
        total_price = cart.calculate_total_price()
        context["total_price"] = total_price
        context["total_tax"] = round((total_price * 9) / 100)
        return context

    def form_valid(self, form):
        user = self.request.user
        address_id = self.request.POST.get('address_id')
        cart = CartModels.objects.get(user=user)
        cart_items = CartItemsModels.objects.filter(cart=cart)

        if not address_id:
            form.add_error(None, "لطفاً یک آدرس انتخاب کنید.")
            return self.form_invalid(form)

        total_price = cart.calculate_total_price()
        tax = round((total_price * 9) / 100)
        final_price = total_price + tax

        # 1. ساخت سفارش
        order = OrderModels.objects.create(
            user=user,
            address=UserAddressModel.objects.get(id=address_id),
            total_price=total_price,
            tax=tax,
            final_price=final_price,
        )

        # 2. افزودن آیتم‌ها به سفارش
        for item in cart_items:
            OrderItemModels.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price,
            )

        # 3. پاک کردن سبد خرید
        cart_items.delete()

        return redirect(self.success_url)
# ======================================================================================================================
class OrderCompleteView(HasCustomerPermission,LoginRequiredMixin,TemplateView):
    template_name = 'order/complete.html'

# ======================================================================================================================