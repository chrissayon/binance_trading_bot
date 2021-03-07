import os
import sys
import logging
from dotenv import load_dotenv
from binance_manager import BinanceManager

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# Load environmental variables
load_dotenv()
api_key = os.getenv('API_KEY')
api_secret = os.getenv('SECRET_KEY')

# Initialize client
binance_manager = BinanceManager(api_key, api_secret)

# get market depth
binance_manager.set_coin("DOGEAUD")

# get order book
# order_book = binance_manager.get_order_book(99)
# print(binance_manager.order_book_asks)
# print(binance_manager.order_book_bids)

# get candlestick data
candlestick_data = binance_manager.get_candlestick_data(99)
print(candlestick_data)