import requests
from django.views import View
from django.shortcuts import get_object_or_404, render
from django.conf import settings
from order.models import PaymentModels, OrderModels


# ======================================================================================================================
class ZarinpalVerifyView(View):
    def get(self, request):
        authority = request.GET.get("Authority")
        status = request.GET.get("Status")

        if not authority:
            return render(request, "payment/failed.html",
                          {"message": "اطلاعات پرداخت ناقص است."})

        payment = get_object_or_404(PaymentModels, authority=authority)

        if status != "OK":
            payment.status = 2
            payment.save()
            return render(request, "order/failed.html",
                          {"message": "پرداخت توسط کاربر لغو شد."})

        payload = {
            "MerchantID": settings.MERCHANT_ID,
            "Amount": int(payment.amount),
            "Authority": authority,
        }
        headers = {"Content-Type": "application/json"}

        response = requests.post(
            "https://sandbox.zarinpal.com/pg/rest/WebGate/PaymentVerification.json",
            json=payload,
            headers=headers,
        )
        result = response.json()

        if result.get("Status") == 100:
            payment.status = 1
            payment.save()

            order = get_object_or_404(OrderModels, payment=payment)
            order.is_paid = True
            order.save()

            return render(request, "payment/complete.html", {"order": order})
        else:
            payment.status = 2
            payment.save()
            return render(request, "payment/complete.html",
                          {"message": "پرداخت تایید نشد."})


# ======================================================================================================================
