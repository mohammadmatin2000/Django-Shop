from django.views.generic import View, TemplateView
from .cart import CartSession
from shop.models import ProductModels
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# ======================================================================================================================
@method_decorator(csrf_exempt, name='dispatch')
class CartAddProductsView(View):
    def post(self, request):
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))
        if product_id:
            cart_session = CartSession(request)
            cart_session.add_product(product_id, quantity)
        else:
            return JsonResponse({"error": "product_id is required"}, status=400)

        return JsonResponse({
            "cart": cart_session.get_products(),
        })
# ======================================================================================================================
class CartSummaryView(TemplateView):
    template_name = 'cart/cart-summary.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = CartSession(self.request)
        cart_items = []
        total_price = 0

        for item in cart.get_products():
            try:
                product = ProductModels.objects.get(id=item['product_id'])
                quantity = item['quantity']
                price = getattr(product, 'discount_price', None) or product.price
                total = price * quantity
                total_price += total
                cart_items.append({
                    'product': product,
                    'quantity': quantity,
                    'quantity_str': str(quantity),
                    'price': price,
                    'total': total,
                })
            except ProductModels.DoesNotExist:
                continue

        context.update({
            'items': cart_items,
            'total_price': total_price,
            'total': total_price,
        })
        return context
# ======================================================================================================================
class CartDeleteView(View):
    def post(self, request):
        product_id = request.POST.get('product_id')
        if product_id:
            cart_session = CartSession(request)
            cart_session.remove_product(product_id)
        else:
            return JsonResponse({"error": "product_id is required"}, status=400)

        return JsonResponse({
            "cart": cart_session.get_products(),
        })
# ======================================================================================================================
class CartUpdateQuantityView(View):
    def post(self, request):
        product_id = request.POST.get('product_id')
        try:
            quantity = int(request.POST.get('quantity', 1))
        except ValueError:
            return JsonResponse({"error": "Invalid quantity"}, status=400)

        if not product_id:
            return JsonResponse({"error": "product_id is required"}, status=400)

        cart_session = CartSession(request)
        cart_session.update_quantity(product_id, quantity)

        return JsonResponse({
            "status": "ok",
            "cart": cart_session.get_products(),
        })
# ======================================================================================================================