from django.db import models
from django.utils.text import slugify
from decimal import Decimal
from ckeditor.fields import RichTextField
from django.urls import reverse

# ======================================================================================================================
class ProductStatusModels(models.IntegerChoices):
    publish = 1, "فعال"
    draft = 2, "غیرفعال"


# ======================================================================================================================
class ProductCategoryModels(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# ======================================================================================================================
class ProductModels(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    category = models.ManyToManyField(ProductCategoryModels, blank=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True, unique=True)
    image = models.ImageField(
        upload_to="images/", null=True, blank=True, default="images/default.jpg"
    )
    description = RichTextField()
    brief_description = models.TextField(null=True, blank=True)
    stock = models.PositiveIntegerField(default=0)
    avg_rate = models.FloatField(default=0)
    status = models.IntegerField(
        choices=ProductStatusModels.choices, default=ProductStatusModels.publish
    )
    price = models.DecimalField(max_digits=10, decimal_places=0)
    discount_percent = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(ProductModels, self).save(*args, **kwargs)

    def is_discounted(self):
        return self.discount_percent > 0

    @property
    def discount_price(self):
        if self.is_discounted():
            discount_amount = (Decimal(self.discount_percent) / 100) * self.price
            return self.price - discount_amount
        return self.price

    def get_price(self):
        return self.discount_price if self.discount_price else self.price

    def is_status(self):
        return self.status == ProductStatusModels.publish

    def get_absolute_url(self):
        return reverse("shop:products-detail",  kwargs={"slug": self.slug})

    def __str__(self):
        return self.title


# ======================================================================================================================
class ProductImageModels(models.Model):
    product = models.ForeignKey("shop.ProductModels", on_delete=models.CASCADE)
    file = models.ImageField(upload_to="images/", null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


# ======================================================================================================================
class WishListModels(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    product = models.ForeignKey("shop.ProductModels", on_delete=models.CASCADE)

    def __str__(self):
        return self.product.title


# ======================================================================================================================
