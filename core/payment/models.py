from django.db import models


# ======================================================================================================================
class PaymentStatusModels(models.IntegerChoices):
    pending = 0, "در انتطار"
    success = 1, "موفقیت"
    failed = 2, "شکست خورده"


# ======================================================================================================================
class PaymentModels(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    callback_url = models.URLField()
    description = models.TextField()
    mobile = models.TextField()
    email = models.TextField()
    status = models.IntegerField(
        choices=PaymentStatusModels.choices,
        default=PaymentStatusModels.pending)
    authority = models.CharField(max_length=255, null=True, blank=True)
    ref_id = models.CharField(max_length=255, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description


# ======================================================================================================================
