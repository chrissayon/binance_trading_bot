from binance.client import Client

class BinanceManager:
    def __init__(self, api_key, api_secret):
        self.BinanceClient = Client(api_key, api_secret)
        pass