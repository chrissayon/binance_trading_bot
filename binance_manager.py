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
        Set coin to use
        """
        self.coin = coin
        return self.coin
