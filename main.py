import os
from dotenv import load_dotenv

from binance.client import Client

# Load environmental variables
load_dotenv()
api_key = os.getenv('API_KEY')
api_secret = os.getenv('SECRET_KEY')

# Initialize client
client = Client(api_key, api_secret)

# get market depth
depth = client.get_order_book(symbol='BNBBTC')
print(depth)