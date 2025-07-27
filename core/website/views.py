from django.views.generic import TemplateView
from shop.models import ProductModels, ProductStatusModels


# ======================================================================================================================
class IndexView(TemplateView):
    template_name = "website/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = ProductModels.objects.filter(
            status=ProductStatusModels.publish.value
        )
        return context


# ======================================================================================================================
class AboutView(TemplateView):
    template_name = "website/about.html"


# ======================================================================================================================
class ContactView(TemplateView):
    template_name = "website/contact.html"


# ======================================================================================================================
