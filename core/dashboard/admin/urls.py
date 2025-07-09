from django.urls import path,include
from .views import AdminDashboardHomeView,AdminSecurityView
# ======================================================================================================================
app_name='admin'
urlpatterns = [
    path('home/',AdminDashboardHomeView.as_view(),name='home'),
    path('security/',AdminSecurityView.as_view(),name='security'),
]
# ======================================================================================================================