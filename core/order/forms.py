from django import forms
from .models import CouponModels


# ======================================================================================================================
class OrderCreateForm(forms.Form):
    address_id = forms.IntegerField(required=True)
    coupon_code = forms.CharField(required=False, max_length=50)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

    def clean_address_id(self):
        from .models import UserAddressModel

        address_id = self.cleaned_data.get("address_id")
        if not UserAddressModel.objects.filter(
                id=address_id, user=self.user).exists():
            raise forms.ValidationError("آدرس انتخاب شده معتبر نیست.")
        return address_id

    def clean_coupon_code(self):
        code = self.cleaned_data.get("coupon_code")
        if not code:
            return code  # کپن وارد نشده، مشکلی نیست

        try:
            coupon = CouponModels.objects.get(code=code)
        except CouponModels.DoesNotExist:
            raise forms.ValidationError("کد کپن یافت نشد.")

        if not coupon.is_valid():
            raise forms.ValidationError("کپن منقضی شده است.")

        if self.user in coupon.used_by.all():
            raise forms.ValidationError(
                "شما قبلاً از این کپن استفاده کرده‌اید.")

        return code


# ======================================================================================================================
