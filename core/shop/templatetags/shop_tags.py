from django import template
from ..models import ProductModels, ProductStatusModels
from shop.models import WishListModels

register = template.Library()


# ======================================================================================================================
@register.inclusion_tag("includes/latest-products.html", takes_context=True)
def latest_products(context):
    user = context["request"].user
    products = ProductModels.objects.filter(
        status=ProductStatusModels.publish.value
    ).order_by("-created_date")[:8]

    wishlist_items = []
    if user.is_authenticated:
        wishlist_items = list(
            WishListModels.objects.filter(user=user).values_list(
                "product__id", flat=True
            )
        )

    return {
        "products": products,
        "wishlist_items": wishlist_items,
        "request": context["request"],
    }


# ======================================================================================================================
@register.inclusion_tag("includes/similar-products.html", takes_context=True)
def similar_products(context, product):
    request = context.get("request")
    user = getattr(request, "user", None)

    products_category = product.category.all()

    base_queryset = (
        ProductModels.objects.filter(
            status=ProductStatusModels.publish.value, category__in=products_category
        )
        .exclude(id=product.id)
        .distinct()
    )

    similar_products = list(base_queryset[:4])

    if len(similar_products) < 4:
        needed = 4 - len(similar_products)
        extra_products = (
            ProductModels.objects.filter(status=ProductStatusModels.publish.value)
            .exclude(id__in=[p.id for p in similar_products] + [product.id])
            .order_by("-created_date")[:needed]
        )
        similar_products.extend(extra_products)

    wishlist_items = []
    if user and user.is_authenticated:
        wishlist_items = list(
            WishListModels.objects.filter(user=user).values_list(
                "product__id", flat=True
            )
        )

    return {
        "products": similar_products,
        "wishlist_items": wishlist_items,
        "request": context["request"],
    }


# ======================================================================================================================
@register.filter
def formatted_price(value):
    try:
        value = float(value)
        formatted = f"{value:,.3f}".replace(",", "٬").replace(".", "٫")
        return f"{formatted} تومان"
    except (ValueError, TypeError):
        return value


# ======================================================================================================================
@register.filter
def times(number):
    try:
        return range(int(number))
    except:
        return []


# ======================================================================================================================
@register.filter
def get_rate_value(dictionary, rate):
    key = f"rate_{rate}"
    return dictionary.get(key, 0)


# ======================================================================================================================
