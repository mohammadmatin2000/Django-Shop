from django.urls import path
from .views import ProductsGridView,ProductsDetailView
# ======================================================================================================================
app_name = "shop"
urlpatterns = [
    path("products/grid/", ProductsGridView.as_view(), name="products-grid"),
    path('products/detail/<slug:slug>/', ProductsDetailView.as_view(), name='products-detail'),
]
# ======================================================================================================================