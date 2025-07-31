from django.contrib.sitemaps import Sitemap
from .models import ProductModels, ProductStatusModels


# ======================================================================================================================
class ProductSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return ProductModels.objects.filter(
            status=ProductStatusModels.publish.value)

    def lastmod(self, obj):
        return obj.updated_date


# ======================================================================================================================
