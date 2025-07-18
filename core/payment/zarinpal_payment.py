import requests
import json

class ZarinpalPayment:
    payment_request_url="https://api.zarinpal.com/pg/v4/payment/request.json"
    payment_verify_url = "https://api.zarinpal.com/pg/v4/payment/verify.json"
    payment_page_url = "https://api.zarinpal.com/pg/v4/payment/page.json"
    def payment_request(self):
        payment_request=requests.get(self.payment_request_url)
        url = "https://api.zarinpal.com/pg/v4/payment/request.json"

        payload = json.dumps({
            "merchant_id": "4ced0a1e-4ad8-4309-9668-3ea3ae8e8897",
            "amount": "1010",
            "callback_url": "http://redreseller.com/verify",
            "description": "افزایش اعتبار کاربر شماره ۱۱۳۴۶۲۹",
            "metadata": {
                "mobile": "09195523234",
                "email": "info.davari@gmail.com"
            }
        })
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

    def payment_verify(self):
        payment_verify=requests.get(self.payment_verify_url)

        url = "https://api.zarinpal.com/pg/v4/payment/verify.json"

        payload = json.dumps({
            "merchant_id": "4ced0a1e-4ad8-4309-9668-3ea3ae8e8897",
            "amount": "1000",
            "authority": "A00000000000000000000000000000000002"
        })
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

    def payment_page(self):
        payment_page=requests.get(self.payment_page_url)

