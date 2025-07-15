from django.db import models
from django.utils import timezone
from shop.models import ProductModels
# ======================================================================================================================
class OrderStatus(models.IntegerChoices):
    PENDING = 1, "در انتظار"
    SUCCESS = 2, "موفق"
    FAILED = 3, "ناموفق"
# ======================================================================================================================
class Coupon(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2)
    max_usage_limit = models.PositiveIntegerField(verbose_name="حداکثر دفعات استفاده")
    used_by = models.ManyToManyField("accounts.User", blank=True)
    expiration_date = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def is_valid(self):
        return self.expiration_date >= timezone.now().date()
    def __str__(self):
        return f"{self.code} - {self.discount_percent}%"
# ======================================================================================================================

class Order(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.PROTECT, related_name="orders")
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.IntegerField(choices=OrderStatus.choices, default=OrderStatus.PENDING)
    coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True, blank=True, related_name="orders")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Order #{self.pk} by {self.user}"
# ======================================================================================================================
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(ProductModels, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def total_price(self):
        return self.price * self.quantity
    def __str__(self):
        return f"{self.quantity} x {self.product.title}"
# ======================================================================================================================