import numpy as np
from binance.client import Client
from datetime import datetime

default_coin = "BTCUSD"

class BinanceManager:
    def __init__(self, api_key, api_secret):
        """
        Initialize client with api and secret key
        """
        self.binance_client = Client(api_key, api_secret)
        self.coin = default_coin
 
    def set_coin(self, coin):
        """
        Set coin to use, else default is BTCUSD
        """
        self.coin = coin
        return self.coin

    def get_order_book(self, number_of_records=100):
        """
        Get order book and split it into bids and asks
        """
        # Check if number of records is in any of the following, otherwise quit function
        number_error_check = { 5, 10, 20, 50, 100, 500, 1000, 5000 }

        if number_of_records not in number_error_check:
            raise Exception('Invalid number of records, should be: 5, 10, 20, 50, 100, 500, 1000 or 5000. ' + \
            'Value of number was {}'.format(number_of_records))
        
        self.order_book = self.binance_client.get_order_book(symbol=self.coin, limit=number_of_records)
        self.order_book_bids = [list(map(float, ask)) for ask in self.order_book['bids']]
        self.order_book_asks = [list(map(float, ask)) for ask in self.order_book['asks']]
        self.order_book_update_id = [int(self.order_book['lastUpdateId'])]
        return self.order_book

    def get_candlestick_data(self, number_of_candlesticks):
        """
        Get candle stick data 
        """
        self.candlestick_data_raw = self.binance_client.get_klines(
            symbol = self.coin, 
            interval = self.binance_client.KLINE_INTERVAL_12HOUR,
            limit = number_of_candlesticks
        )

        self.candlestick_data_int = [list(map(float, ask)) for ask in self.candlestick_data_raw]

        self.candlestick_data_np = np.array(self.candlestick_data_int)
        self.candlestick_open_time_points = self.candlestick_data_np[:, 0]
        self.candlestick_datetime_open_time_points = [datetime.fromtimestamp(time/1000) for time in self.candlestick_open_time_points]
        self.candlestick_open_points = self.candlestick_data_np[:, 1]
        self.candlestick_high_points = self.candlestick_data_np[:, 2]
        self.candlestick_low_points = self.candlestick_data_np[:, 3]
        self.candlestick_close_points = self.candlestick_data_np[:, 4]
        self.candlestick_volume_points = self.candlestick_data_np[:, 5]
        self.candlestick_close_time_points = self.candlestick_data_np[:, 6]
        self.candlestick_datetime_close_time_points = [datetime.fromtimestamp(time/1000) for time in self.candlestick_close_time_points]
        self.candlestick_quote_asset_points = self.candlestick_data_np[:, 7]
        self.candlestick_trade_number_points = self.candlestick_data_np[:, 8]
        self.candlestick_buy_base_asset_volume_points = self.candlestick_data_np[:, 9]
        self.candlestick_buy_quote_asset_volume_points = self.candlestick_data_np[:, 10]
        self.candlestick_ignored_points = self.candlestick_data_np[:, 11]
        
        return self.candlestick_data_int