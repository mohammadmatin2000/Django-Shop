from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, TemplateView, View
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages

from .permission import HasCustomerPermission
from .models import UserAddressModel, OrderModels, OrderItemModels, CouponModels
from cart.models import CartModels,CartItemsModels
from .forms import OrderCreateForm
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
        total_price = cart.calculate_total_price()
        tax = round((total_price * 9) / 100)
        final_price = total_price + tax

        coupon_code = self.request.session.get("coupon_code")
        coupon = None
        discount = 0

        if coupon_code:
            try:
                coupon = CouponModels.objects.get(code=coupon_code)

                if not coupon.is_valid():
                    messages.warning(self.request, "کد تخفیف منقضی شده است.")
                    self.request.session.pop("coupon_code", None)

                elif self.request.user in coupon.used_by.all():
                    messages.warning(self.request, "شما قبلاً از این کد استفاده کرده‌اید.")
                    self.request.session.pop("coupon_code", None)

                else:
                    discount = round((total_price * coupon.discount_percent) / 100)
                    final_price -= discount
                    final_price = max(final_price, 0)

            except CouponModels.DoesNotExist:
                self.request.session.pop("coupon_code", None)

        context.update({
            "addresses": UserAddressModel.objects.filter(user=self.request.user),
            "total_price": total_price,
            "total_tax": tax,
            "final_price": final_price,
            "coupon": coupon,
            "discount": discount,
            "checked_coupon_code": coupon_code,
        })
        return context

    def form_valid(self, form):
        user = self.request.user
        cart = get_object_or_404(CartModels, user=user)
        cart_items = CartItemsModels.objects.filter(cart=cart)

        address_id = form.cleaned_data.get('address_id')
        coupon_code = self.request.session.get('coupon_code')

        total_price = cart.calculate_total_price()
        tax = round((total_price * 9) / 100)
        final_price = total_price + tax

        coupon = None
        if coupon_code:
            try:
                coupon = CouponModels.objects.get(code=coupon_code)

                if not coupon.is_valid() or user in coupon.used_by.all():
                    coupon = None
                    self.request.session.pop("coupon_code", None)

                else:
                    discount = round((total_price * coupon.discount_percent) / 100)
                    final_price -= discount
                    final_price = max(final_price, 0)

            except CouponModels.DoesNotExist:
                self.request.session.pop("coupon_code", None)

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
            self.request.session.pop("coupon_code", None)

        cart_items.delete()
        messages.success(self.request, "سفارش با موفقیت ثبت شد.")
        return redirect(self.success_url)
# ======================================================================================================================
class CheckCouponView(View):
    def post(self, request, *args, **kwargs):
        code = request.POST.get("coupon_code", "").strip()
        user = request.user

        request.session.pop("coupon_code", None)

        if not code:
            messages.error(request, "کد تخفیف نمی‌تواند خالی باشد.")
            return redirect("order:checkout")

        try:
            coupon = CouponModels.objects.get(code=code)

            if not coupon.is_valid():
                messages.error(request, "❌ این کد تخفیف منقضی شده است.")
            elif user in coupon.used_by.all():
                messages.warning(request, "❌ شما قبلاً از این کد استفاده کرده‌اید.")
            else:
                request.session["coupon_code"] = coupon.code
                messages.success(
                    request,
                    f"✅ کد '{coupon.code}' با {coupon.discount_percent}% تخفیف معتبر است.",
                )
        except CouponModels.DoesNotExist:
            messages.error(request, "❌ کد تخفیف یافت نشد.")

        return redirect("order:checkout")

# ======================================================================================================================
class OrderCompleteView(HasCustomerPermission, LoginRequiredMixin, TemplateView):
    template_name = 'order/complete.html'
# ======================================================================================================================