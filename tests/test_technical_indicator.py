import pytest
import os, sys, inspect
from binance_trading_bot.technical_indicators import TechnicalIndicators

crypto_trading_instance = TechnicalIndicators()

class TestTechnicalIndicators:
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

    def test_calculate_support(self):
        """
        Test support function
        """
        bid_data = [
            [1, 1],
            [1, 1]
        ]

        support_data = crypto_trading_instance.calculate_support(bid_data)

        assert support_data == 1


    def test_calculate_trendline(self):
        """
        Test trendline function
        """
        time_points = [1, 2, 3, 4]
        data_points = [1, 1, 1, 1]

        trendline_equation = crypto_trading_instance.calculate_trendline(time_points, data_points, 0)

        assert trendline_equation.all() == [1]

    def test_calculate_rsi(self):
        """
        Test rsi function
        """
        candlestick_data = [
            [
                0, # Open time
                1, # Open
                0, # High
                0, # Low
                2, # Close
                0, # Volume
                0, # Close time
                0, # Quote asset volume
                0, # Number of trades
                0, # Taker buy base asset volume
                0, # Taker buy quote asset volume
                0  # Can be ignored
            ],
            [
                0, # Open time
                2, # Open
                0, # High
                0, # Low
                3, # Close
                0, # Volume
                0, # Close time
                0, # Quote asset volume
                0, # Number of trades
                0, # Taker buy base asset volume
                0, # Taker buy quote asset volume
                0  # Can be ignored
            ],
            [
                0, # Open time
                3, # Open
                0, # High
                0, # Low
                2, # Close
                0, # Volume
                0, # Close time
                0, # Quote asset volume
                0, # Number of trades
                0, # Taker buy base asset volume
                0, # Taker buy quote asset volume
                0  # Can be ignored
            ],
            [
                0, # Open time
                2, # Open
                0, # High
                0, # Low
                1, # Close
                0, # Volume
                0, # Close time
                0, # Quote asset volume
                0, # Number of trades
                0, # Taker buy base asset volume
                0, # Taker buy quote asset volume
                0  # Can be ignored
            ]
        ]

        rsi_data = crypto_trading_instance.calculate_rsi(candlestick_data)

        assert rsi_data == 50



