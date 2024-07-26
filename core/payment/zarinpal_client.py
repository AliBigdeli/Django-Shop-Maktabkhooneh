import requests
import json
from django.conf import settings


def get_domain():
    # for fixing issue with the sites model before migration
    try:
        from django.contrib.sites.models import Site
        return Site.objects.get_current().domain
    except:
        return "example.com"


def get_protocol():
    # Determine the protocol based on the SECURE_SSL_REDIRECT setting
    return 'https' if getattr(settings, 'SECURE_SSL_REDIRECT', False) else 'http'


class ZarinPalSandbox:
    _payment_request_url = "https://sandbox.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
    _payment_verify_url = "https://sandbox.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
    _payment_page_url = "https://sandbox.zarinpal.com/pg/StartPay/"
    _callback_url = f"{get_protocol()}://{get_domain()}/payment/verify"

    def __init__(self, merchant_id=settings.MERCHANT_ID):
        self.merchant_id = merchant_id

    def payment_request(self, amount, description="پرداختی کاربر"):
        payload = {
            "MerchantID": self.merchant_id,
            "Amount": str(amount),
            "CallbackURL": self._callback_url,
            "Description": description,
        }
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.post(
            self._payment_request_url, headers=headers, data=json.dumps(payload))

        return response.json()

    def payment_verify(self, amount, authority):
        payload = {
            "MerchantID": self.merchant_id,
            "Amount": amount,
            "Authority": authority
        }
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.post(
            self._payment_verify_url, headers=headers, data=json.dumps(payload))
        return response.json()

    def generate_payment_url(self, authority):
        return f"{self._payment_page_url}{authority}"
