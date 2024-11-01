from dotenv import load_dotenv
import os
import requests

load_dotenv()

class PaydouniaAPI:
    BASE_URL = "https://app.paydunya.com/sandbox-api/v1/checkout-invoice/create"

    def __init__(self):
        self.master_key = os.getenv("PAYDOUNIA_MASTER_KEY")
        self.private_key = os.getenv("PAYDOUNIA_PRIVATE_KEY")
        self.token = os.getenv("PAYDOUNIA_TOKEN")

    def create_invoice(self, amount, currency, description):
        url = self.BASE_URL
        headers = {
            "Content-Type": "application/json"
        }
        data = {
            "invoice": {
                "total_amount": amount,
                "currency": currency,
                "description": description
            },
            "MASTER_KEY": self.master_key,
            "PRIVATE_KEY": self.private_key,
            "TOKEN": self.token
        }

        response = requests.post(url, headers=headers, json=data)
        return response.json()
