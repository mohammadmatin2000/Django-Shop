from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _

# ======================================================================================================================
class CustomAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_verified:
            raise ValidationError(
                "حساب کاربری شما هنوز تایید نشده است.",
                code='inactive',
            )

# ======================================================================================================================
class SetPasswordForm(forms.Form):
    """
    A form that lets a user set their password without entering the old
    password
    """

    error_messages = {
        "password_mismatch": _("The two password fields didn’t match."),
    }
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password", "class": "form-control"}
        ),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password", "class": "form-control"}
        ),
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get("new_password1")
        password2 = self.cleaned_data.get("new_password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages["password_mismatch"],
                code="password_mismatch",
            )
        password_validation.validate_password(password2, self.user)
        return password2

    def save(self, commit=True):
        password = self.cleaned_data["new_password1"]
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user
# ======================================================================================================================
