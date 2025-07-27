from django import forms
from .models import ReviewModels


# ======================================================================================================================
class SubmitReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewModels
        fields = ["rate", "description"]


# ======================================================================================================================
