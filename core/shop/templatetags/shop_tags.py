from django import template

register = template.Library()
from ..models import ProductModels, ProductStatusModels
# ======================================================================================================================
@register.inclusion_tag('includes/latest-products.html')
def latest_products():
    products = ProductModels.objects.filter(status=ProductStatusModels.publish.value).order_by('-created_date')[:8]
    return {'products': products}
# ======================================================================================================================
@register.inclusion_tag('includes/similar-products.html')
def similar_products(product):
    products_category = product.category.all()
    products = ProductModels.objects.filter(status=ProductStatusModels.publish.value,
                                            category__in=products_category).order_by('-created_date')[:4]
    return {'products': products}
# ======================================================================================================================
@register.filter
def formatted_price(value):
    try:
        value = float(value)
        formatted = f"{value:,.3f}".replace(".", "٬").replace(".", "٫")
        return f"{formatted} تومان"
    except (ValueError, TypeError):
        return value
# ======================================================================================================================