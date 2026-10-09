import requests
import json

url = (
    "https://api.coingecko.com/api/v3/simple/price"
    "?ids=bitcoin,ethereum,ripple,solana"
    "&vs_currencies=usd"
)

response = requests.get(url)
data = response.json()

print(json.dumps(data, indent=2))
