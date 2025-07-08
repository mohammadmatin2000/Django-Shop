from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from accounts.models import UserType

# ======================================================================================================================
class DashboardHomeView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        print("User type:", request.user.type)  # یا logging
        if request.user.type == UserType.customer.value:
            return redirect(reverse_lazy('dashboard:customer:home'))
        elif request.user.type == UserType.admin.value:
            return redirect(reverse_lazy('dashboard:admin:home'))
        else:
            print("Redirecting to login because of unknown user type.")
            return redirect(reverse_lazy('accounts:login'))

    def get(self, request, *args, **kwargs):
        return self.dispatch(request, *args, **kwargs)
# ======================================================================================================================