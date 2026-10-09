import requests

url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

response = requests.get(url)

print("HTTP Status:", response.status_code)
print("Response:")
print(response.text)
