from django.contrib import admin
from .models import CouponModels, OrderModels, OrderItemModels
# ======================================================================================================================
class OrderItemInline(admin.TabularInline):
    model = OrderItemModels
    extra = 0
    readonly_fields = ['price', 'quantity', 'product']
    can_delete = False
# ======================================================================================================================
@admin.register(OrderModels)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'status', 'total_price', 'created_date', 'updated_date']
    list_filter = ['status', 'created_date', 'updated_date']
    search_fields = ['user__email', 'user__username', 'address', 'city', 'zip_code']
    date_hierarchy = 'created_date'
    inlines = [OrderItemInline]
    readonly_fields = ['created_date', 'updated_date']
    autocomplete_fields = ['user', 'coupon']
# ======================================================================================================================
@admin.register(CouponModels)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'discount_percent', 'expiration_date', 'max_usage_limit', 'created_date']
    search_fields = ['code']
    list_filter = ['expiration_date', 'created_date']
    readonly_fields = ['created_date', 'updated_date']
    filter_horizontal = ['used_by']
# ======================================================================================================================
@admin.register(OrderItemModels)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'price', 'quantity', 'created_date']
    search_fields = ['order__id', 'product__title']
    list_filter = ['created_date']
    readonly_fields = ['created_date', 'updated_date']
    autocomplete_fields = ['order', 'product']
# ======================================================================================================================