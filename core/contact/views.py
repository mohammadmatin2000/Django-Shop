from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ContactForm, NewsletterForm
from django.views import View
from django.shortcuts import redirect
# ======================================================================================================================
class ContactView(FormView):
    template_name = 'website/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact:contact-us')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "پیام شما با موفقیت ارسال شد.")
        return super().form_valid(form)
# ======================================================================================================================
class NewsletterSubscribeView(View):
    def post(self, request, *args, **kwargs):
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "عضویت شما در خبرنامه انجام شد.")
        else:
            messages.error(request, "ایمیل معتبر وارد کنید یا قبلاً عضو شده‌اید.")
        return redirect(request.META.get('HTTP_REFERER', '/'))
# ======================================================================================================================