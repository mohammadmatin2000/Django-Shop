from django.urls import path
from .views import ContactView, NewsletterSubscribeView

# ======================================================================================================================
app_name = "contact"
urlpatterns = [
    path("contact-us/", ContactView.as_view(), name="contact-us"),
    path("newsletter/", NewsletterSubscribeView.as_view(), name="newsletter"),
]
# ======================================================================================================================
