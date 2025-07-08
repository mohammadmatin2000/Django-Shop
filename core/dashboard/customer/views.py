from django.views.generic import TemplateView
# ======================================================================================================================
class CustomerDashboardHomeView(TemplateView):
    template_name = "dashboard/customer/home.html"
# ======================================================================================================================