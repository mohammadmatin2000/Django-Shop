from django.contrib import admin
from .models import ProductModels,ProductImageModels,ProductCategoryModels
# ======================================================================================================================
@admin.register(ProductModels)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'status','price','created_date', 'updated_date')  # نمایش برخی از فیلدهای محصول
    search_fields = ('title', 'description')  # جستجو بر اساس نام و توضیحات
    list_filter = ('category', 'created_date')  # فیلتر کردن محصولات بر اساس دسته‌بندی و تاریخ ایجاد
    ordering = ('-created_date',)  # مرتب‌سازی محصولات بر اساس تاریخ ایجاد به صورت نزولی
    prepopulated_fields = {'slug': ('title',)}  # پر کردن خودکار فیلد slug بر اساس نام
    date_hierarchy = 'created_date'  # امکان فیلتر بر اساس تاریخ

# ======================================================================================================================
@admin.register(ProductCategoryModels)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('title','created_date')  # نمایش نام، والد، وضعیت فعال بودن و تاریخ ایجاد
    search_fields = ('title',)  # جستجو بر اساس نام دسته‌بندی
    list_filter = ('created_date',)  # فیلتر بر اساس وضعیت فعال بودن و تاریخ ایجاد
    prepopulated_fields = {'slug': ('title',)}  # پر کردن خودکار slug بر اساس نام

# ======================================================================================================================
@admin.register(ProductImageModels)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product','created_date')  # نمایش محصول، تصویر، وضعیت برجسته بودن و تاریخ ایجاد
    list_filter = ('created_date',)  # فیلتر بر اساس وضعیت برجسته بودن و تاریخ ایجاد

# ======================================================================================================================