from django.views.generic import View,TemplateView
from .cart import CartSession
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# ======================================================================================================================
@method_decorator(csrf_exempt, name='dispatch')
class SessionAddProductsView(View):
    def post(self, request):
        product_id = request.POST.get('product_id')
        if product_id:
            cart_session = CartSession(request)
            cart_session.add_product(product_id)
        return JsonResponse({
            "cart": cart_session.get_add_product(),
        })
# ======================================================================================================================
class CartSummaryView(TemplateView):
    template_name = 'cart/cart-summary.html'
# ======================================================================================================================