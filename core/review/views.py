from django.views import View
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from .models import ReviewModels
from shop.models import ProductModels
from .forms import SubmitReviewForm
from django.contrib.auth.mixins import LoginRequiredMixin

# ======================================================================================================================
class SubmitReviewView(LoginRequiredMixin, View):
    def post(self, request, product_id):
        product = get_object_or_404(ProductModels, id=product_id)
        form = SubmitReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
            messages.success(request, "نظر شما ثبت شد.")
        else:
            messages.error(request, "خطا در ثبت نظر.")

        return redirect('shop:products-detail', slug=product.slug)
# ======================================================================================================================