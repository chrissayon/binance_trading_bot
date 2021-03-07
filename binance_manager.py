from binance.client import Client

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
        self.order_book_bids = self.order_book['bids']
        self.order_book_asks = self.order_book['asks']
        self.order_book_update_id = self.order_book['lastUpdateId']
        return self.order_book

    def get_candlestick_data(self, number_of_candlesticks):
        """
        Get candle stick data 
        """
        self.candlestick_data = self.binance_client.get_klines(
            symbol = self.coin, 
            interval = self.binance_client.KLINE_INTERVAL_12HOUR,
            limit = number_of_candlesticks
        )

        return self.candlestick_data