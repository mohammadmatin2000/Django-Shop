from django.contrib.auth import forms as auth_forms
from django import forms
from django.utils.translation import gettext_lazy as _
from accounts.models import Profile
from shop.models import ProductModels

# ======================================================================================================================
class AdminPasswordChangeForm(auth_forms.PasswordChangeForm):
    error_messages = {
        **auth_forms.PasswordChangeForm.error_messages,
        "password_incorrect": _(
            "پسورد فعلی را اشتباه وارد کردید لطفا صحیح وارد کنید"
        ),
        "password_mismatch": _("پسورد های جدید با هم مطابقت ندارند"),
    }
# ======================================================================================================================
class AdminChangeProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("first_name", "last_name", "phone_number", "image")
# ======================================================================================================================
class AdminUpdateProductForm(forms.ModelForm):
    class Meta:
        model = ProductModels
        fields = (
        "category",
        "title",
        "slug",
        "image",
        "description",
        "brief_description",
        "stock",
        "status",
        "discount_percent",
        "price"
        )
# ======================================================================================================================