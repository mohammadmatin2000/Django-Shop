from django.db import models
from django.utils import timezone
from shop.models import ProductModels
from payment.models import PaymentModels
from accounts.models import Profile


# ======================================================================================================================
class OrderStatusModels(models.IntegerChoices):
    PENDING = 1, "در انتظار"
    SUCCESS = 2, "موفق"
    FAILED = 3, "ناموفق"


# ======================================================================================================================
class CouponModels(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2)
    max_usage_limit = models.PositiveIntegerField()
    used_by = models.ManyToManyField("accounts.User", blank=True)
    expiration_date = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def is_valid(self):
        return self.expiration_date >= timezone.now().date()

    def __str__(self):
        return f"{self.code} - {self.discount_percent}%"


# ======================================================================================================================
class UserAddressModel(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    address = models.CharField(max_length=250)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.address}"


# ======================================================================================================================
class OrderModels(models.Model):
    user = models.ForeignKey(
        "accounts.User", on_delete=models.PROTECT, related_name="orders"
    )
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    payment = models.ForeignKey(
        PaymentModels, on_delete=models.SET_NULL, null=True, blank=True
    )
    tax = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    final_price = models.DecimalField(
        max_digits=10, decimal_places=0, default=0)
    total_price = models.DecimalField(max_digits=12, decimal_places=0)
    status = models.IntegerField(
        choices=OrderStatusModels.choices, default=OrderStatusModels.PENDING
    )
    coupon = models.ForeignKey(
        CouponModels,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders",
    )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.pk} by {self.user}"

    @property
    def get_status(self):
        return {
            "value": self.status,
            "label": dict(
                OrderStatusModels.choices).get(
                self.status,
                "نامشخص"),
        }

    @property
    def is_successful(self):
        return self.status == OrderStatusModels.SUCCESS

    @property
    def get_price(self):

        return sum(item.get_total_price for item in self.items.all())

    @property
    def get_price_with_discount(self):
        price = self.get_price
        if self.coupon and self.coupon.is_valid():
            discount_amount = price * (self.coupon.discount_percent / 100)
            return price - discount_amount
        return price

    @property
    def get_full_address(self):
        return f"{self.address}، {self.city}، {self.state}"

    def get_full_name(self):
        return f"{self.profile.first_name} {self.profile.last_name}"


# ======================================================================================================================
class OrderItemModels(models.Model):
    order = models.ForeignKey(
        OrderModels, on_delete=models.CASCADE, related_name="items"
    )
    product = models.ForeignKey(
        ProductModels, on_delete=models.PROTECT, related_name="product_items"
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2
    )  # قیمت واحد در زمان خرید
    quantity = models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.title}"

    @property
    def get_total_price(self):
        return self.price * self.quantity


# ======================================================================================================================
