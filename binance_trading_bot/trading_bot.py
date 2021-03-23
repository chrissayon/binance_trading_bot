import os
import sys
import logging
import time
import constants
from dotenv import load_dotenv
from binance_manager import BinanceManager
from technical_indicators import TechnicalIndicators

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# Load environmental variables
load_dotenv('../.env')
api_key = os.getenv('API_KEY')
api_secret = os.getenv('SECRET_KEY')

# Initialize client
binance_instance = BinanceManager(api_key, api_secret)
binance_instance.set_coin("DOGEAUD")

# Initialize stock trading manager
technical_instance = TechnicalIndicators()


def execute():
    while True:
        binance_instance.get_candlestick_data(10)
        technical_instance.calculate_rsi(binance_instance.candlestick_data_int)
        print(technical_instance.rsi)
        time.sleep(1)

execute()