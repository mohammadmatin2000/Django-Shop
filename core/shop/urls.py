from django.urls import path
from .views import ProductGridView
# ======================================================================================================================
app_name = "shop"
urlpatterns = [
    path("product/grid/", ProductGridView.as_view(), name="product-grid"),
]