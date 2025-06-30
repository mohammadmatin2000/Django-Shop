from django.urls import path
from .views import ProductsGridView
# ======================================================================================================================
app_name = "shop"
urlpatterns = [
    path("products/grid/", ProductsGridView.as_view(), name="products-grid"),
]
# ======================================================================================================================