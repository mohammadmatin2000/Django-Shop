from django.contrib.auth import forms as auth_forms
from django.utils.translation import gettext_lazy as _
# ======================================================================================================================
class PasswordChangeForm(auth_forms.PasswordChangeForm):
    error_messages = {
        **auth_forms.PasswordChangeForm.error_messages,
        "password_incorrect": _(
            "پسورد فعلی را اشتباه وارد کردید لطفا صحیح وارد کنید"
        ),
        "password_mismatch": _("پسورد های جدید با هم مطابقت ندارند"),
    }
# ======================================================================================================================