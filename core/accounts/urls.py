from django.urls import path
from django.contrib.auth import views as auth_views
from .views import LoginView, LogoutView,SignupView
from .forms import SetPasswordForm
# ======================================================================================================================
app_name = 'accounts'
urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # path('register/', Register.as_view(), name='register'),
    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(
            template_name="accounts/reset_password/reset_password.html"
        ),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="accounts/reset_password/reset_password_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="accounts/reset_password/reset_password_form.html",
            form_class=SetPasswordForm,
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="accounts/reset_password/reset_password_complete.html"
        ),
        name="password_reset_complete",
    ),
]
# ======================================================================================================================
