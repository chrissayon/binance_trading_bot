import os, sys, logging
from dotenv import load_dotenv
from binance_manager import BinanceManager

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# Load environmental variables
load_dotenv()
api_key = os.getenv('API_KEY')
api_secret = os.getenv('SECRET_KEY')

# Initialize client
binanceManager = BinanceManager(api_key, api_secret)
# client = Client(api_key, api_secret)

# get market depth
# depth = client.get_order_book(symbol='BNBBTC')bina