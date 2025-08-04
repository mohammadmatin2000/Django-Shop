from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from website.sitemap import StaticViewSitemap
from shop.sitemap import ProductSitemap
# ======================================================================================================================
# دیکشنری نقشه سایت
sitemaps_dict = {
    "static": StaticViewSitemap,   # صفحات ثابت مثل درباره‌ما، تماس با ما
    "products": ProductSitemap     # صفحات محصولات فروشگاه
}
# ======================================================================================================================
# تعریف مسیرهای اصلی پروژه
urlpatterns = [
    path("admin/", admin.site.urls),                    # پنل مدیریت جنگو
    path("", include("website.urls")),                  # صفحات اصلی سایت
    path("accounts/", include("accounts.urls")),        # مدیریت کاربران
    path("shop/", include("shop.urls")),                # فروشگاه
    path("contact/", include("contact.urls")),          # فرم تماس با ما
    path("cart/", include("cart.urls")),                # سبد خرید
    path("dashboard/", include("dashboard.urls")),      # داشبورد مدیریتی
    path("order/", include("order.urls")),              # سفارشات
    path("payment/", include("payment.urls")),          # پرداخت
    path("review/", include("review.urls")),            # نظرات کاربران
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps_dict}, name="sitemap"),  # نقشه سایت
    path("captcha/", include("captcha.urls")),          # کپچا برای فرم‌ها
]
# ======================================================================================================================
# افزودن مسیر فایل‌های رسانه و استاتیک فقط در حالت دیباگ
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# ======================================================================================================================
# افزودن مسیر دیباگ تولبار در حالت دیباگ
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),  # ابزار دیباگ
    ]
# ======================================================================================================================