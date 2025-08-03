from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from website.sitemap import StaticViewSitemap
from shop.sitemap import ProductSitemap
# ======================================================================================================================
sitemaps_dict = {"static": StaticViewSitemap, "products": ProductSitemap}
# ======================================================================================================================
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("website.urls")),
    path("accounts/", include("accounts.urls")),
    path("shop/", include("shop.urls")),
    path("contact/", include("contact.urls")),
    path("cart/", include("cart.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("order/", include("order.urls")),
    path("payment/", include("payment.urls")),
    path("review/", include("review.urls")),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps_dict}, name="sitemap"),
    path('captcha/', include('captcha.urls')),
]
# ======================================================================================================================
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
# ======================================================================================================================
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
# ======================================================================================================================
