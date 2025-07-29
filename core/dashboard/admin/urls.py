from django.urls import path
from .views import (
    AdminDashboardHomeView,
    AdminSecurityView,
    AdminProfileView,
    AdminProfileImageView,
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
    AdminOrdersInvoiceVIew,
    AdminCommentsListView,
    AdminCommentsUpdateView,
    AdminCommentsDeleteView,
    AdminContactListView,
    AdminContactMessageDetailView,
    AdminContactMessageDeleteView,
    AdminNewsletterListView,
    AdminNewsletterDeleteView,
    AdminNewsletterDetailView,
    AdminUserListView,
    AdminUserListView,
    AdminUserDetailView,
    AdminUserUpdateView,
    AdminUserDeleteView,
)

# ======================================================================================================================
app_name = "admin"
urlpatterns = [
    path("home/", AdminDashboardHomeView.as_view(), name="home"),
    path("security/", AdminSecurityView.as_view(), name="security"),
    path("profile/", AdminProfileView.as_view(), name="profile"),
    path("profile/image/", AdminProfileImageView.as_view(), name="profile-image"),
    path("products/list/", AdminProductListView.as_view(), name="products-list"),
    path(
        "products/<int:pk>/update/",
        AdminProductUpdateView.as_view(),
        name="product-update",
    ),
    path(
        "products/<int:pk>/delete/",
        AdminProductDeleteView.as_view(),
        name="product-delete",
    ),
    path("products/create/", AdminProductCreateView.as_view(), name="product-create"),
    path("coupons/list/", AdminCouponsListView.as_view(), name="coupon-list"),
    path("coupons/create/", AdminCouponCreateView.as_view(), name="coupon-create"),
    path(
        "coupons/<int:pk>/delete/",
        AdminCouponDeleteView.as_view(),
        name="coupon-delete",
    ),
    path(
        "coupons/<int:pk>/update/",
        AdminCouponUpdateView.as_view(),
        name="coupon-update",
    ),
    path("orders/list/", AdminOrdersListView.as_view(), name="orders-list"),
    path(
        "orders/<int:pk>/update/", AdminOrdersUpdateView.as_view(), name="orders-update"
    ),
    path(
        "orders/<int:pk>/invoice/",
        AdminOrdersInvoiceVIew.as_view(),
        name="orders-invoice",
    ),
    path("comments/list/", AdminCommentsListView.as_view(), name="comments-list"),
    path(
        "comments/<int:pk>/update/",
        AdminCommentsUpdateView.as_view(),
        name="comments-update",
    ),
    path(
        "comments/<int:pk>/delete/",
        AdminCommentsDeleteView.as_view(),
        name="comments-delete",
    ),

    path("contact/list/", AdminContactListView.as_view(), name="contact-list"),
    path("contact/<int:pk>/detail/", AdminContactMessageDetailView.as_view(), name="contact-detail"),
    path("contact/<int:pk>/delete/", AdminContactMessageDeleteView.as_view(), name="contact-delete"),

    path("newsletter/list/", AdminNewsletterListView.as_view(), name="newsletter-list"),
    path("newsletter/<int:pk>/detail/", AdminNewsletterDetailView.as_view(), name="newsletter-detail"),
    path("newsletter/<int:pk>/delete/", AdminNewsletterDeleteView.as_view(), name="newsletter-delete"),

    path("users/list/", AdminUserListView.as_view(), name="users-list"),
    path("users/<int:pk>/detail/", AdminUserDetailView.as_view(), name="user-detail"),
    path("users/<int:pk>/edit/", AdminUserUpdateView.as_view(), name="user-update"),
    path("users/<int:pk>/delete/", AdminUserDeleteView.as_view(), name="user-delete"),
]
# ======================================================================================================================
