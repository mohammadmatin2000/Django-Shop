from django import forms
from .models import ContactMessage, NewsletterSubscriber


# ======================================================================================================================
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "last_name", "email", "phone_number", "message"]
        widgets = {
            "message": forms.Textarea(attrs={"rows": 5}),
        }


# ======================================================================================================================
class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ["email"]


# ======================================================================================================================
