from django.contrib.auth import forms as auth_forms
from django.core.exceptions import ValidationError
# ======================================================================================================================
class AuthenticationForm(auth_forms.AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_verified:
            raise ValidationError(
                "حساب کاربری شما هنوز تایید نشده است.",
                code='inactive',
            )
# ======================================================================================================================