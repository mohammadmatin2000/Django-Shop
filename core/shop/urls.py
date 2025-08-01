from django.urls import path, re_path
from .views import ProductsGridView, ProductsDetailView, AddToWishlistView

# ======================================================================================================================
app_name = "shop"
urlpatterns = [
    path("products/grid/", ProductsGridView.as_view(), name="products-grid"),
    re_path(
        r"^products/detail/(?P<slug>[-\w\u0600-\u06FF]+)/$",
        ProductsDetailView.as_view(),
        name="products-detail",
    ),
    path("wishlist/", AddToWishlistView.as_view(), name="add-to-wishlist"),
]
# ======================================================================================================================
