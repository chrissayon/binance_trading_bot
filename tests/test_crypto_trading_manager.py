import pytest
import os,sys,inspect
from binance_trading_bot.crypto_trading_manager import CryptoTradingManager

crypto_trading_instance = CryptoTradingManager()

class TestClassCyptoTradingManager:
    def test_calculate_resistance(self):
        """
        Test resistance function
        """
        ask_data = [
            [1, 1],
            [1, 1]
        ]

        resistance_data = crypto_trading_instance.calculate_resistance(ask_data)

        assert resistance_data == 1

    def test_calculate_trendline(self):
        """
        Test trendline function
        """
        time_points = [1, 2, 3, 4]
        data_points = [1, 1, 1, 1]

        trendline_equation = crypto_trading_instance.calculate_trendline(time_points, data_points, 0)

        assert trendline_equation.all() == [1] 
