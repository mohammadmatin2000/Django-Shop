from django.urls import path
from .views import SubmitReviewView

# ======================================================================================================================
app_name = "review"
urlpatterns = [
    path(
        "submit/review/<int:product_id>/",
        SubmitReviewView.as_view(),
        name="submit-review",
    ),
]
# ======================================================================================================================
