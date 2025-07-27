from django.urls import path
from .views import (
    OrderCheckOutView,
    OrderCompleteView,
    CheckCouponView,
    OrderFailedView,
)

# ======================================================================================================================
app_name = "order"
urlpatterns = [
    path("checkout/", OrderCheckOutView.as_view(), name="checkout"),
    path("complete/", OrderCompleteView.as_view(), name="complete"),
    path("failed/", OrderFailedView.as_view(), name="failed"),
    path("coupon/checout/", CheckCouponView.as_view(), name="coupon-checkout"),
]
# ======================================================================================================================
