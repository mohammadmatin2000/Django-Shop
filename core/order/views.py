from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from .permission import HasCustomerPermission
from .models import UserAddressModel, OrderModels, OrderItemModels, CouponModels
from .forms import OrderCreateForm
from cart.models import CartModels, CartItemsModels
# ======================================================================================================================
class OrderCheckOutView(HasCustomerPermission, LoginRequiredMixin, FormView):
    template_name = 'order/checkout.html'
    form_class = OrderCreateForm
    success_url = reverse_lazy('order:complete')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = CartModels.objects.get(user=self.request.user)
        context["addresses"] = UserAddressModel.objects.filter(user=self.request.user)
        total_price = cart.calculate_total_price()
        context["total_price"] = total_price
        context["total_tax"] = round((total_price * 9) / 100)
        return context

    def form_valid(self, form):
        user = self.request.user
        cart = get_object_or_404(CartModels, user=user)
        cart_items = CartItemsModels.objects.filter(cart=cart)

        address_id = form.cleaned_data.get('address_id')
        coupon_code = form.cleaned_data.get('coupon_code')

        total_price = cart.calculate_total_price()
        tax = round((total_price * 9) / 100)
        final_price = total_price + tax

        coupon = None
        if coupon_code:
            try:
                coupon = CouponModels.objects.get(code=coupon_code)
            except CouponModels.DoesNotExist:
                messages.error(self.request, "کد کپن وجود ندارد.")
                return self.form_invalid(form)

            if not coupon.is_valid():
                messages.error(self.request, "کپن منقضی شده است.")
                return self.form_invalid(form)

            if user in coupon.used_by.all():
                messages.error(self.request, "شما قبلاً از این کپن استفاده کرده‌اید.")
                return self.form_invalid(form)


            discount = (total_price * coupon.discount_percent) / 100
            final_price -= discount
            final_price = max(final_price, 0)


        order = OrderModels.objects.create(
            user=user,
            address=get_object_or_404(UserAddressModel, id=address_id, user=user),
            total_price=total_price,
            tax=tax,
            final_price=final_price,
            coupon=coupon if coupon else None,
        )

        for item in cart_items:
            OrderItemModels.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price,
            )
        if coupon:
            coupon.used_by.add(user)


        cart_items.delete()

        messages.success(self.request, "سفارش با موفقیت ثبت شد.")
        return redirect(self.success_url)


# ======================================================================================================================
class OrderCompleteView(HasCustomerPermission, LoginRequiredMixin, TemplateView):
    template_name = 'order/complete.html'
# ======================================================================================================================