from django.urls import path
from .views import CartAddProductsView,CartSummaryView,CartDeleteView,CartUpdateQuantityView
# ======================================================================================================================
app_name = 'cart'
urlpatterns = [
    path("add/products/", CartAddProductsView.as_view(), name="add-products"),
    path("delete/products/", CartDeleteView.as_view(), name="delete-products"),
    path("update/quantity/", CartUpdateQuantityView.as_view(), name="update-quantity"),
    path("cart/summary/", CartSummaryView.as_view(), name="cart-summary"),
]
# ======================================================================================================================