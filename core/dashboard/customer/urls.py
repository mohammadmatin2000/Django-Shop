from django.urls import path
from .views import (CustomerDashboardHomeView,CustomerSecurityDashboardView,CustomerProfileDashboardView,
                    CustomerProfileImageDashboardView,
                    CustomerAddressListView,
                    CustomerAddressEditView,
                    CustomerAddressDeleteView,
                    CustomerAddressCreateView)
# ======================================================================================================================
app_name='customer'
urlpatterns = [
    path('home/',CustomerDashboardHomeView.as_view(),name='home'),
    path('security/',CustomerSecurityDashboardView.as_view(),name='security'),
    path('profile/',CustomerProfileDashboardView.as_view(),name='profile'),
    path('profile/image/',CustomerProfileImageDashboardView.as_view(),name='profile-image'),

    path('address/list/',CustomerAddressListView.as_view(),name='address-list'),
    path('address/<int:pk>/edit/',CustomerAddressEditView.as_view(),name='address-edit'),
    path('address/<int:pk>/delete/',CustomerAddressDeleteView.as_view(),name='address-delete'),
    path('address/create/',CustomerAddressCreateView.as_view(),name='address-create'),
]
# ======================================================================================================================