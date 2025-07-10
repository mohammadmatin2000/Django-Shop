from django.urls import path
from .views import AdminDashboardHomeView,AdminSecurityView,AdminProfileView,AdminProfileImageView
# ======================================================================================================================
app_name='admin'
urlpatterns = [
    path('home/',AdminDashboardHomeView.as_view(),name='home'),
    path('security/',AdminSecurityView.as_view(),name='security'),
    path('profile/',AdminProfileView.as_view(),name='profile'),
    path('profile/image/',AdminProfileImageView.as_view(),name='profile-image'),
]
# ======================================================================================================================