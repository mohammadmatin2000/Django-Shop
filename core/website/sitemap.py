from django.contrib import sitemaps
from django.urls import reverse


# ======================================================================================================================
class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.3
    changefreq = "monthly"

    def items(self):
        return ["index", "about", "contact"]

    def location(self, item):

        return reverse(f"website:{item}")


# ======================================================================================================================
