from django.urls import path
from .views import SessionAddProductsView,CartSummaryView
# ======================================================================================================================
app_name = 'cart'
urlpatterns = [
    path("add/products/", SessionAddProductsView.as_view(), name="add-products"),
    path("cart/summary/", CartSummaryView.as_view(), name="cart-summary"),
]
# ======================================================================================================================