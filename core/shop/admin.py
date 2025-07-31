from django.contrib import admin
from .models import (
    ProductModels,
    ProductImageModels,
    ProductCategoryModels,
    WishListModels,
)


# ======================================================================================================================
@admin.register(ProductModels)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "status",
        "avg_rate",
        "price",
        "created_date",
        "updated_date",
    )  # نمایش برخی از فیلدهای محصول
    search_fields = ("title", "description")  # جستجو بر اساس نام و توضیحات
    list_filter = (
        "category",
        "created_date",
    )  # فیلتر کردن محصولات بر اساس دسته‌بندی و تاریخ ایجاد
    # مرتب‌سازی محصولات بر اساس تاریخ ایجاد به صورت نزولی
    ordering = ("-created_date",)
    # پر کردن خودکار فیلد slug بر اساس نام
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "created_date"  # امکان فیلتر بر اساس تاریخ


# ======================================================================================================================
@admin.register(ProductCategoryModels)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "created_date",
    )  # نمایش نام، والد، وضعیت فعال بودن و تاریخ ایجاد
    search_fields = ("title",)  # جستجو بر اساس نام دسته‌بندی
    # فیلتر بر اساس وضعیت فعال بودن و تاریخ ایجاد
    list_filter = ("created_date",)
    # پر کردن خودکار slug بر اساس نام
    prepopulated_fields = {"slug": ("title",)}


# ======================================================================================================================
@admin.register(ProductImageModels)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "created_date",
    )  # نمایش محصول، تصویر، وضعیت برجسته بودن و تاریخ ایجاد
    # فیلتر بر اساس وضعیت برجسته بودن و تاریخ ایجاد
    list_filter = ("created_date",)


# ======================================================================================================================
@admin.register(WishListModels)
class WishListModelsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "product",
    )  # نمایش محصول، تصویر، وضعیت برجسته بودن و تاریخ ایجاد
    list_filter = ("user",)  # فیلتر بر اساس وضعیت برجسته بودن و تاریخ ایجاد


# ======================================================================================================================
