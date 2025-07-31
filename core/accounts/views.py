from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomAuthenticationForm, CustomSignupForm
from .utils.email_thread import EmailThread


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
class CustomPasswordResetView(PasswordResetView):
    email_template_name = "accounts/rest_password/password_reset_email.html"
    success_url = reverse_lazy("password_reset_done")

    def form_valid(self, form):

        opts = {
            "use_https": self.request.is_secure(),
            "token_generator": self.token_generator,
            "from_email": self.from_email,
            "email_template_name": self.email_template_name,
            "subject_template_name": self.subject_template_name,
            "request": self.request,
        }
        email = form.cleaned_data["email"]
        for user in self.get_users(email):
            context = self.get_email_context(user)
            subject = self.get_subject()
            message = self.get_message(user, context)
            EmailThread(
                subject, message, self.from_email, [
                    user.email]).start()
        return super().form_valid(form)


# ======================================================================================================================
