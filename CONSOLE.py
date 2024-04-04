import requests
import hmac
import hashlib
import time

api =''
secret  = ''

def get_binance_price(api, secret, symbol):
    # Binance API endpoint for getting current price
    url = 'https://api.binance.com/api/v3/ticker/price'

    # Current timestamp in milliseconds
    timestamp = int(time.time() * 1000)

    # Construct query parameters
    query_string = f'symbol={symbol}&timestamp={timestamp}'
    
    # Create signature
    signature = hmac.new(secret.encode(), query_string.encode(), hashlib.sha256).hexdigest()

    # Request headers
    headers = {
        'X-MBX-APIKEY': api
    }

    # Request parameters
    params = {
        'symbol': symbol,
        'timestamp': timestamp,
        'signature': signature
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            print(f"Current price of {symbol}: {data['price']}")
        else:
            print("Failed to retrieve price information. Status code:", response.status_code)
    except Exception as e:
        print("Error occurred:", e)

# Specify the symbol you want to get the price for, e.g., 'BTCUSDT' for Bitcoin/USDT pair
symbol = 'BTCUSDT'

get_binance_price(api, secret, symbol)
