from django.urls import path,include
from .views import AdminDashboardHomeView
# ======================================================================================================================
app_name='admin'
urlpatterns = [
    path('home/',AdminDashboardHomeView.as_view(),name='home'),
]
# ======================================================================================================================