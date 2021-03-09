import pytest
import os,sys,inspect
from binance_trading_bot.crypto_trading_manager import CryptoTradingManager

crypto_trading_instance = CryptoTradingManager()

class TestClassCyptoTradingManager:
    def test_calculate_current_resistance(self):
        """
        Test resistance function
        """
        ask_data = [
            [1, 1],
            [1, 1]
        ]

        resistance_data = crypto_trading_instance.calculate_current_resistance(ask_data)

        assert resistance_data == 1