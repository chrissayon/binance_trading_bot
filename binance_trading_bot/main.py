import os
import sys
import logging
import constants
from dotenv import load_dotenv
from binance_manager import BinanceManager
from crypto_trading_manager import CryptoTradingManager

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# Load environmental variables
load_dotenv()
api_key = os.getenv('API_KEY')
api_secret = os.getenv('SECRET_KEY')

# Initialize client
binance_instance = BinanceManager(api_key, api_secret)

# Initialize stock trading manager
cypto_trading_instance = CryptoTradingManager()

# set coin
binance_instance.set_coin("DOGEAUD")



# get order book
# order_book = binance_instance.get_order_book(100)
# print(binance_instance.order_book_asks)
# print(binance_instance.order_book_bids)
# print(cypto_trading_instance.calculate_current_resistance(binance_instance.order_book_asks))
# print(cypto_trading_instance.calculate_current_support(binance_instance.order_book_bids))

# get candlestick data
# candlestick_data = binance_instance.get_candlestick_data(2)
# print(candlestick_data)
# print())




# get candlestick data
candlestick_data = binance_instance.get_candlestick_data(14)

# print(binance_instance.candlestick_open_time_points)
# print(binance_instance.candlestick_high_points)

# trend_line = cypto_trading_instance.calculate_trendline(
#     binance_instance.candlestick_open_time_points,
#     binance_instance.candlestick_high_points,
# )
# print(cypto_trading_instance.trend_line)

# cypto_trading_instance.calculate_all_trendline(binance_instance.candlestick_dict)

# cypto_trading_instance.graph_trendline()


cypto_trading_instance.calculate_rsi(binance_instance.candlestick_data_int)
cypto_trading_instance.localize_rsi_to_coin(binance_instance.candlestick_data_int)
cypto_trading_instance.graph_candlesticks(
    # binance_instance.candlestick_open_time_points,
    binance_instance.candlestick_dict[constants.CANDLESTICK_DATETIME_OPEN],
    binance_instance.candlestick_open_points,
    binance_instance.candlestick_high_points,
    binance_instance.candlestick_low_points,
    binance_instance.candlestick_close_points,
)
