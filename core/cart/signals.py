from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from .cart import CartSession
# ======================================================================================================================
@receiver(user_logged_in)
def post_login(sender, user, request, **kwargs):
    cart = CartSession(request)
    cart.sync_cart_items_from_db(user)
# ======================================================================================================================
def pre_logout(sender, user, request, **kwargs):
    cart = CartSession(request)
    cart.merge_session_cart_in_db(user)
# ======================================================================================================================