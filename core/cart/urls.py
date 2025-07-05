from django.urls import path
from .views import SessionAddProductsView
# ======================================================================================================================
app_name = 'cart'
urlpatterns = [
    path("add/products/", SessionAddProductsView.as_view(), name="add-products"),
]
# ======================================================================================================================