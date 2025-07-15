from django.urls import path
from .views import OrderCheckOutView
# ======================================================================================================================
app_name = 'order'
urlpatterns = [
    path('checkout/', OrderCheckOutView.as_view(), name='checkout'),
]
# ======================================================================================================================