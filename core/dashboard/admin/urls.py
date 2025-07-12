from django.urls import path
from .views import (AdminDashboardHomeView, AdminSecurityView, AdminProfileView, AdminProfileImageView,
                    AdminProductListView,
                    AdminProductUpdateView,
                    AdminProductDeleteView,
                    AdminProductCreateView)
# ======================================================================================================================
app_name='admin'
urlpatterns = [
    path('home/',AdminDashboardHomeView.as_view(),name='home'),
    path('security/',AdminSecurityView.as_view(),name='security'),
    path('profile/',AdminProfileView.as_view(),name='profile'),
    path('profile/image/',AdminProfileImageView.as_view(),name='profile-image'),
    path('products/list/',AdminProductListView.as_view(),name='products-list'),
    path("products/<int:pk>/update/",AdminProductUpdateView.as_view(),name='product-update'),
    path("products/<int:pk>/delete/",AdminProductDeleteView.as_view(),name='product-delete'),
    path("products/create/",AdminProductCreateView.as_view(),name='product-create'),
]
# ======================================================================================================================