import requests

try:
    response = requests.get("https://api.binance.com/api/v3/time", timeout=10)
    print("✅ Binance API is reachable.")
    print("🕒 Server time:", response.json())
except requests.exceptions.RequestException as e:
    print("❌ Connection failed:", e)
