from ..settings import *
# ======================================================================================================================
# امنیت پروژه
SECRET_KEY = config("SECRET_KEY", default="")  # کلید مخفی برای امنیت پروژه
DEBUG = config("DEBUG", default=True, cast=bool)  # حالت دیباگ فقط برای توسعه
ALLOWED_HOSTS = ["*"]  # لیست میزبان‌های مجاز
# ======================================================================================================================
# تنظیمات پایگاه داده
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",  # استفاده از PostgreSQL
        "NAME": config("PG_NAME", default="default_database"),
        "USER": config("PG_USER", default="username"),
        "PASSWORD": config("PG_PASSWORD", default="password"),
        "HOST": config("PG_HOST", default="db"),
        "PORT": config("PG_PORT", cast=int, default=5432),
    }
}
# ======================================================================================================================
# فعال‌سازی HSTS برای جلوگیری از حملات Man-in-the-Middle (مدت زمان 1 ساعت)
SECURE_HSTS_SECONDS = 3600
# ریدایرکت خودکار تمام درخواست‌ها از HTTP به HTTPS
SECURE_SSL_REDIRECT = True
# فعال‌سازی کوکی‌های امن فقط برای اتصال‌های HTTPS در نشست کاربران
SESSION_COOKIE_SECURE = True
# فعال‌سازی کوکی امن برای CSRF فقط روی HTTPS
CSRF_COOKIE_SECURE = True
# ======================================================================================================================