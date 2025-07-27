import requests
import json
from django.conf import settings


class ZarinpalPayment:
    BASE_URL = "https://api.zarinpal.com/pg/v4/payment/"
    MERCHANT_ID = settings.MERCHANT_ID

    def __init__(self, amount, callback_url, description, mobile="", email=""):
        self.amount = amount
        self.callback_url = callback_url
        self.description = description
        self.metadata = {
            "mobile": str(mobile),  # مطمئن شو رشته باشه
            "email": str(email),
        }

    def payment_request(self):
        url = self.BASE_URL + "PaymentRequest.json"
        payload = {
            "merchant_id": self.MERCHANT_ID,
            "amount": self.amount,
            "callback_url": self.callback_url,
            "description": self.description,
            "metadata": self.metadata,
        }
        headers = {"Content-Type": "application/json", "Accept": "application/json"}
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        return response.json()

    def payment_verify(self, authority):
        url = self.BASE_URL + "PaymentVerification.json"
        payload = {
            "merchant_id": self.MERCHANT_ID,
            "amount": self.amount,
            "authority": authority,
        }
        headers = {"Content-Type": "application/json", "Accept": "application/json"}
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        return response.json()

    def get_gateway_url(self, authority):
        return f"https://sandbox.zarinpal.com/pg/StartPay/{authority}"
