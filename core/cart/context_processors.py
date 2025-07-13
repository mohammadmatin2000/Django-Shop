from .models import CartModels
# ======================================================================================================================
def cart_item_count(request):
    if request.user.is_authenticated:
        cart = CartModels.objects.filter(user=request.user).first()
        if cart:
            total_quantity = sum(item.quantity for item in cart.items.all())
        else:
            total_quantity = 0
    else:
        total_quantity = 0
    return {
        'total_quantity': total_quantity
    }
# ======================================================================================================================