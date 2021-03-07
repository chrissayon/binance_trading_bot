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

    def get_order_book(self):
        """
        Get order book and split it into bids and asks
        """
        self.order_book = self.binance_client.get_order_book(symbol=self.coin)
        self.order_book_bids = self.order_book['bids']
        self.order_book_asks = self.order_book['asks']
        self.order_book_update_id = self.order_book['lastUpdateId']
        return self.order_book