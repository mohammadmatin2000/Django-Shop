from django.contrib.auth import views as auth_views
from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomAuthenticationForm, CustomSignupForm
# ======================================================================================================================
class SignupView(View):
    def get(self, request):
        form = CustomSignupForm()
        return render(request, "accounts/signup.html", {"form": form})

    def post(self, request):
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "ثبت‌نام با موفقیت انجام شد! اکنون وارد شوید.")
            return redirect("accounts:login")
        return render(request, "accounts/signup.html", {"form": form})
# ======================================================================================================================
class LoginView(auth_views.LoginView):
    template_name = "accounts/login.html"
    redirect_authenticated_user = True
    form_class = CustomAuthenticationForm
# ======================================================================================================================
class LogoutView(auth_views.LogoutView):
    pass
# ======================================================================================================================