from django.urls import path
from .views import (AdminDashboardHomeView, AdminSecurityView, AdminProfileView, AdminProfileImageView,
                    AdminProductListView,
                    AdminProductUpdateView,
                    AdminProductDeleteView,
                    AdminProductCreateView,
                    AdminCouponsListView,
                    AdminCouponCreateView,
                    AdminCouponDeleteView,
                    AdminCouponUpdateView,
                    AdminOrdersListView,
                    AdminOrdersUpdateView,
                    AdminOrdersInvoiceVIew)
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

    path('coupons/list/',AdminCouponsListView.as_view(),name='coupon-list'),
    path('coupons/create/',AdminCouponCreateView.as_view(),name='coupon-create'),
    path('coupons/<int:pk>/delete/',AdminCouponDeleteView.as_view(),name='coupon-delete'),
    path('coupons/<int:pk>/update/',AdminCouponUpdateView.as_view(),name='coupon-update'),

    path('orders/list/',AdminOrdersListView.as_view(),name='orders-list'),
    path('orders/<int:pk>/update/',AdminOrdersUpdateView.as_view(),name='orders-update'),
    path('orders/<int:pk>/invoice/',AdminOrdersInvoiceVIew.as_view(),name='orders-invoice'),

]
# ======================================================================================================================