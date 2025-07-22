from django.contrib.auth.decorators import login_required
from .models import CartModels,CartItemsModels
from django.views.generic import View, TemplateView
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from shop.models import ProductModels
# ======================================================================================================================
@method_decorator([csrf_exempt, login_required], name='dispatch')
class CartAddProductsView(View):
    def post(self, request):
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))

        if not product_id:
            return JsonResponse({"error": "product_id is required"}, status=400)

        product = ProductModels.objects.filter(id=product_id).first()
        if not product:
            return JsonResponse({"error": "محصول یافت نشد"}, status=404)

        cart, _ = CartModels.objects.get_or_create(user=request.user)
        item, created = CartItemsModels.objects.get_or_create(cart=cart, product=product)
        if not created:
            item.quantity += quantity
        else:
            item.quantity = quantity
        item.save()

        return JsonResponse({"status": "محصول اضافه شد"})
# ======================================================================================================================
@method_decorator([csrf_exempt, login_required], name='dispatch')
class CartDeleteView(View):
    def post(self, request):
        product_id = request.POST.get('product_id')

        if not product_id:
            return JsonResponse({"error": "product_id is required"}, status=400)

        cart = CartModels.objects.filter(user=request.user).first()
        if not cart:
            return JsonResponse({"error": "سبد خرید یافت نشد"}, status=404)

        CartItemsModels.objects.filter(cart=cart, product_id=product_id).delete()

        return JsonResponse({"status": "محصول حذف شد"})
# ======================================================================================================================
@method_decorator([csrf_exempt, login_required], name='dispatch')
class CartUpdateQuantityView(View):
    def post(self, request):
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))

        cart = CartModels.objects.filter(user=request.user).first()
        if not cart:
            return JsonResponse({"error": "سبد خرید یافت نشد"}, status=404)

        item = CartItemsModels.objects.filter(cart=cart, product_id=product_id).first()
        if item:
            item.quantity = quantity
            item.save()

        return JsonResponse({"status": "بروزرسانی انجام شد"})
# ======================================================================================================================
class CartSummaryView(TemplateView):
    template_name = 'cart/cart-summary.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        cart = CartModels.objects.filter(user=self.request.user).first()
        cart_items = []
        total_price = 0

        if cart:
            for item in cart.items.select_related('product'):
                product = item.product
                price = product.discount_price or product.price
                total = price * item.quantity
                total_price += total
                cart_items.append({
                    'product': product,
                    'quantity': item.quantity,
                    'price': price,
                    'total': total,
                })

        context.update({
            'items': cart_items,
            'total_price': total_price,
            'total': total_price,
        })
        return context
# ======================================================================================================================