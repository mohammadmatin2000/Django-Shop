from django.urls import path
from .views import CustomerDashboardHomeView,CustomerSecurityDashboardView,CustomerProfileDashboardView,CustomerProfileImageDashboardView
# ======================================================================================================================
app_name='customer'
urlpatterns = [
    path('home/',CustomerDashboardHomeView.as_view(),name='home'),
    path('security/',CustomerSecurityDashboardView.as_view(),name='security'),
    path('profile/',CustomerProfileDashboardView.as_view(),name='profile'),
    path('profile/image/',CustomerProfileImageDashboardView.as_view(),name='profile-image'),
]
# ======================================================================================================================