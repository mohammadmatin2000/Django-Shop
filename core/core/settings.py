# مسیر اصلی پروژه
from pathlib import Path
from decouple import config
# ======================================================================================================================
BASE_DIR = Path(__file__).resolve().parent.parent  # مسیر ریشه پروژه
# ======================================================================================================================
# برنامه‌های نصب‌شده در پروژه
INSTALLED_APPS = [
    # اپ‌های پیش‌فرض جنگو
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",

    # اپلیکیشن‌های داخلی پروژه
    "website", "accounts", "shop", "contact", "cart",
    "dashboard", "order", "payment", "review",

    # اپ‌های جانبی
    "widget_tweaks", "ckeditor", "debug_toolbar",
    "django.contrib.sitemaps", "django.contrib.sites",
    "storages", "captcha",
]
# ======================================================================================================================
# تنظیمات کپچا
MULTI_CAPTCHA_ADMIN = {
    'engine': 'simple-captcha'  # استفاده از کپچای ساده
}
# ======================================================================================================================
SITE_ID = 1  # شناسه سایت برای سیستم چندسایتی جنگو
# ======================================================================================================================
# میان‌افزارها
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]
# ======================================================================================================================
# مسیر اصلی URLها
ROOT_URLCONF = "core.urls"
# ======================================================================================================================
# تنظیمات قالب‌ها (Templates)
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # مسیر قالب‌های HTML
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [  # پردازشگرهای قالب برای دسترسی به اطلاعات مختلف
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "cart.context_processors.cart_item_count",  # شمارش آیتم‌های سبد خرید
            ],
        },
    },
]
# ======================================================================================================================
WSGI_APPLICATION = "core.wsgi.application"  # ورود به اپلیکیشن WSGI
# ======================================================================================================================

# اعتبارسنجی رمز عبور کاربران
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]
# ======================================================================================================================
# تنظیمات محلی‌سازی و منطقه زمانی
LANGUAGE_CODE = "en-us"  # زبان پیش‌فرض
TIME_ZONE = config("TIME_ZONE", default="UTC")  # منطقه زمانی
USE_I18N = True  # فعال‌سازی ترجمه
USE_TZ = True  # استفاده از منطقه زمانی
# ======================================================================================================================
# تنظیمات فایل‌های استاتیک و مدیا
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]
MEDIA_ROOT = BASE_DIR / "media"
# ======================================================================================================================
# تنظیمات اتصال به MinIO برای فایل‌های مدیا
AWS_ACCESS_KEY_ID = 'minioadmin'  # شناسه دسترسی
AWS_SECRET_ACCESS_KEY = 'minioadmin'  # کلید مخفی
AWS_STORAGE_BUCKET_NAME = 'mybucket'  # نام باکت در MinIO
AWS_S3_ENDPOINT_URL = 'http://minio:9000'  # آدرس داخلی
MEDIA_URL = 'http://127.0.0.1:9000/mybucket/'  # آدرس عمومی برای نمایش فایل‌ها
DEFAULT_FILE_STORAGE = 'core.storage_backends.PublicMediaStorage'  # استوریج سفارشی
# ======================================================================================================================
SECURE_SSL_REDIRECT = False  # عدم استفاده از ریدایرکت SSL در توسعه
# ======================================================================================================================
# تنظیمات ایمیل برای ارسال پیام‌ها
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = config("EMAIL_HOST", default="smtp.gmail.com")
EMAIL_PORT = config("EMAIL_PORT", default=587, cast=int)
EMAIL_HOST_USER = config("EMAIL_HOST_USER", default="")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", default="...")  # رمز عبور ایمیل
EMAIL_USE_TLS = config("EMAIL_USE_TLS", default=True, cast=bool)
EMAIL_USE_SSL = config("EMAIL_USE_SSL", default=False, cast=bool)
DEFAULT_FROM_EMAIL = "mohammadmatin13872008@gmail.com"  # ایمیل پیش‌فرض فرستنده
PASSWORD_RESET_TIMEOUT = 60 * 60 * 48  # زمان انقضای لینک بازیابی رمز (48 ساعت)
# ======================================================================================================================
# تنظیمات مدل کاربر سفارشی
AUTH_USER_MODEL = "accounts.User"
LOGIN_REDIRECT_URL = "/"  # مسیر پس از ورود
LOGOUT_REDIRECT_URL = "/"  # مسیر پس از خروج
# ======================================================================================================================
# اطلاعات درگاه پرداخت زرین‌پال
MERCHANT_ID = config("MERCHANT_ID", default="...")
ZARINPAL_MERCHANT_ID = "..."
ZARINPAL_CALLBACK_URL = "http://127.0.0.1:8000/payment/verify/"  # آدرس برگشت پس از پرداخت
# ======================================================================================================================
# آی‌پی‌های داخلی برای دیباگ تولبار
INTERNAL_IPS = [
    "127.0.0.1",
    "172.18.0.1",
    "172.18.0.4",
    "172.20.10.5",
]
# ======================================================================================================================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"  # تنظیم فیلد پیش‌فرض برای مدل‌ها
# ======================================================================================================================
