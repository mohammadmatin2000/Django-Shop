from django.contrib import admin
from .models import ContactMessage, NewsletterSubscriber


# ======================================================================================================================
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "last_name", "email", "phone_number", "created_at")
    search_fields = (
        "name",
        "email",
    )


# ======================================================================================================================
@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ("email", "subscribed_at")
    search_fields = ("email",)


# ======================================================================================================================
