import requests
import json

class ZarinpalPayment:
    BASE_URL = "https://api.zarinpal.com/pg/v4/payment/"
    MERCHANT_ID = "4ced0a1e-4ad8-4309-9668-3ea3ae8e8897"

    def __init__(self, amount, callback_url, description, mobile="", email=""):
        self.amount = amount
        self.callback_url = callback_url
        self.description = description
        self.metadata = {
            "mobile": mobile,
            "email": email
        }

    def payment_request(self):
        url = self.BASE_URL + "request.json"
        payload = {
            "merchant_id": self.MERCHANT_ID,
            "amount": self.amount,
            "callback_url": self.callback_url,
            "description": self.description,
            "metadata": self.metadata,
        }
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        response = requests.post(url, headers=headers, data=json.dumps(payload))
        return response.json()

    def payment_verify(self, authority):
        url = self.BASE_URL + "verify.json"
        payload = {
            "merchant_id": self.MERCHANT_ID,
            "amount": self.amount,
            "authority": authority
        }
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        response = requests.post(url, headers=headers, data=json.dumps(payload))
        return response.json()

    def get_gateway_url(self, authority):
        return f"https://www.zarinpal.com/pg/StartPay/{authority}"


# --- ✅ مثال تست ---
if __name__ == "__main__":
    zp = ZarinpalPayment(
        amount=10000,
        callback_url="https://yoursite.com/verify",
        description="افزایش اعتبار",
        mobile="09123456789",
        email="your@email.com"
    )

    # ارسال درخواست پرداخت
    result = zp.payment_request()
    print("✅ Payment Request Response:")
    print(result)

    if result.get("data") and result["data"].get("authority"):
        authority = result["data"]["authority"]
        print("👉 برای پرداخت، کاربر رو بفرست به این آدرس:")
        print(zp.get_gateway_url(authority))
    else:
        print("❌ مشکلی در ارسال درخواست پرداخت وجود دارد.")
