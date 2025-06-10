import requests
import os
from dotenv import load_dotenv
import json

# Load API key
load_dotenv(dotenv_path=".env.txt")
API_KEY = os.getenv("COINMARKET_API_KEY")

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
symbols = ["BTC", "ETH", "BNB", "XRP", "SOL"]
all_crypto_data = {}

for symbol in symbols:
    params = {"symbol": symbol, "convert": "USD"}
    headers = {"X-CMC_PRO_API_KEY": API_KEY}
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    all_crypto_data[symbol] = data["data"][symbol]

# Save data to JSON
with open("crypto_data.json", "w") as f:
    json.dump(all_crypto_data, f, indent=4)

print("✅ crypto_data.json created successfully")
