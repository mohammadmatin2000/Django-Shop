from django.views.generic import TemplateView
# ======================================================================================================================
class AdminDashboardHomeView(TemplateView):
    template_name = "dashboard/admin/home.html"
# ======================================================================================================================