from django.contrib import admin
from .models import CartModels, CartItemsModels


# ======================================================================================================================
@admin.register(CartModels)
class CartAdmin(admin.ModelAdmin):
    list_display = ["id", "user"]


# ======================================================================================================================
@admin.register(CartItemsModels)
class CartItemsAdmin(admin.ModelAdmin):
    list_display = ["id", "cart", "product", "quantity"]


# ======================================================================================================================
