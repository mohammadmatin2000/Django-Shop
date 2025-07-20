from django.urls import path
from .views import ZarinpalVerifyView
# ======================================================================================================================
app_name = 'payment'
urlpatterns = [
    path('verify/', ZarinpalVerifyView.as_view()),
]
# ======================================================================================================================