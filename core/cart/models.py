from django.db import models

# ======================================================================================================================
class CartModels(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
# ======================================================================================================================
class CartItemsModels(models.Model):
    cart = models.ForeignKey(CartModels, on_delete=models.CASCADE)
    product = models.ForeignKey('shop.ProductModels', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
# ======================================================================================================================