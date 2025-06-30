from django.db import models
# ======================================================================================================================
class ProductStatusView(models.IntegerChoices):
    publish = 1, "فعال"
    draft = 2, "غیر فعال"
# ======================================================================================================================
class ProductCategoryView(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
# ======================================================================================================================
class ProductView(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    category = models.ManyToManyField(ProductCategoryView, blank=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    image = models.ImageField(upload_to="images/", null=True, blank=True, default="images/default.jpg")
    description = models.TextField()
    stock = models.PositiveIntegerField(default=0)
    status = models.IntegerField(choices=ProductStatusView.choices, default=ProductStatusView.publish)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    discount_percent = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
# ======================================================================================================================
