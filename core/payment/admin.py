from django.contrib import admin
from payment.models import PaymentModels


# ======================================================================================================================
@admin.register(PaymentModels)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["amount", "callback_url", "status"]
    list_filter = ["status", "created_date", "updated_date"]
    date_hierarchy = "created_date"


# ======================================================================================================================
