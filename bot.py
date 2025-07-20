from dotenv import load_dotenv
import os
from binance.client import Client
from binance.exceptions import BinanceAPIException

# Load environment
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")

# Print keys para macheck kung nakuha
print("🔐 API Key:", api_key)
print("🔐 API Secret:", api_secret)

# Exit kung wala
if not api_key or not api_secret:
    print("❌ ERROR: API key or secret not loaded properly.")
    exit()

# Connect to Binance
try:
    client = Client(api_key, api_secret)
    account_info = client.get_account()
    print("✅ Successfully connected to Binance!")
    print("📊 Account balances:")
    for balance in account_info['balances']:
        asset = balance['asset']
        free = float(balance['free'])
        if free > 0:
            print(f"{asset}: {free}")
except BinanceAPIException as e:
    print("❌ Binance API Error:", e.message)
except Exception as e:
    print("❌ Connection failed:", str(e))
