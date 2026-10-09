import requests

url = (
    "https://api.coingecko.com/api/v3/simple/price"
    "?ids=bitcoin,ethereum,ripple,solana"
    "&vs_currencies=usd"
)

data = requests.get(url).json()

print("=== CRYPTO DAILY ===")
print()

print(f"BTC : ${data['bitcoin']['usd']}")
print(f"ETH : ${data['ethereum']['usd']}")
print(f"XRP : ${data['ripple']['usd']}")
print(f"SOL : ${data['solana']['usd']}")
