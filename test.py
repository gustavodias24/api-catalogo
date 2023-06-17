import requests
from decouple import config
base = "https://api.mercadopago.com"
headers = {
    "Authorization": "Bearer " + config("TOKEN_MP")
}

resp = requests.get("{}/v1/payments/{}".format(base, "59531690114"), headers=headers)

print(resp.json()["status"])
print(resp.json()["transaction_amount"])