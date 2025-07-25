from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.dispatch import receiver
from django.db.models.signals import post_save
from accounts.models import Profile
# ======================================================================================================================
class ReviewStatusModels(models.IntegerChoices):
    pending = 0,'در حال انتطار'
    accepted = 2, "تایید شده"
    rejected = 3, "رد شده"
# ======================================================================================================================
class ReviewModels(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    product = models.ForeignKey('shop.ProductModels', on_delete=models.CASCADE)
    rate = models.IntegerField(default=5, validators=[
        MinValueValidator(0), MaxValueValidator(5)])
    status = models.IntegerField(choices=ReviewStatusModels.choices, default=ReviewStatusModels.pending.value)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description
# ======================================================================================================================
@receiver(post_save, sender=ReviewModels)
def calculate_avg_review(sender, instance, created, **kwargs):
    pass
# ======================================================================================================================