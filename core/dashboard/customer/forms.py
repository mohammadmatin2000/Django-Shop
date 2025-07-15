from django.contrib.auth import forms as auth_forms
from django import forms
from django.utils.translation import gettext_lazy as _
from accounts.models import Profile
from order.models import UserAddressModel
# ======================================================================================================================
class CustomerPasswordChangeForm(auth_forms.PasswordChangeForm):
    error_messages = {
        **auth_forms.PasswordChangeForm.error_messages,
        "password_incorrect": _(
            "پسورد فعلی را اشتباه وارد کردید لطفا صحیح وارد کنید"
        ),
        "password_mismatch": _("پسورد های جدید با هم مطابقت ندارند"),
    }
# ======================================================================================================================
class CustomerChangeProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("first_name", "last_name", "phone_number", "image")
# ======================================================================================================================
class CustomUserAddressForm(forms.ModelForm):
    class Meta:
        model = UserAddressModel
        fields = [
            "address",
            "state",
            "city",
            "zip_code",
        ]
# ======================================================================================================================