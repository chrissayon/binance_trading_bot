from binance.client import Client

defaultCoin = "BTCUSD"

class BinanceManager:
    def __init__(self, api_key, api_secret):
        """
        Initialize client with api and secret key
        """
        self.binanceClient = Client(api_key, api_secret)
        self.coin = defaultCoin
 
    def set_coin(self, coin):
        """
        Set coin to use
        """
        self.coin = coin
        return self.coin
