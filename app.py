import requests

url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

response = requests.get(url)
data = response.json()

print(f"BTCUSDT = {data['price']}")
