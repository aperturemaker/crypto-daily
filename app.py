import os
import requests
import resend

resend.api_key = os.environ["RESEND_API_KEY"]

url = (
    "https://api.coingecko.com/api/v3/simple/price"
    "?ids=bitcoin,ethereum,ripple,solana"
    "&vs_currencies=usd"
)

data = requests.get(url).json()

report = f"""
<h1>Crypto Daily</h1>

<ul>
<li>BTC : ${data['bitcoin']['usd']}</li>
<li>ETH : ${data['ethereum']['usd']}</li>
<li>XRP : ${data['ripple']['usd']}</li>
<li>SOL : ${data['solana']['usd']}</li>
</ul>
"""

resend.Emails.send({
    "from": "onboarding@resend.dev",
    "to": "aperturemaker@gmail.com",
    "subject": "Crypto Daily Test from GitHub",
    "html": report
})

print("Email sent")
