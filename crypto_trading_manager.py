import numpy as np
import constants
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import binance_manager as BinanceManager

class CryptoTradingManager:
    def __init__(self):
        pass
        
    def calculate_current_resistance(self, ask_orders):
        """
        Calculate current resistance by looking asks in order book
        Orders need to be passed in a [[cryptocurrency_value, othercurrency_totalvalue], ...] format
        """
        self.weight = 0
        self.resistance_total = 0

        #Calculate weighted average
        for ask in ask_orders:
            self.weight += ask[1]
            self.resistance_total += ask[0] * ask[1]

        self.resistance = self.resistance_total/self.weight

        return self.resistance

    def calculate_current_support(self, bid_orders):
        """
        Calculate current support by looking bids in order book
        Orders need to be passed in a [[cryptocurrency_value, othercurrency_totalvalue], ...] format
        """
        self.weight = 0
        self.support_total = 0

        #Calculate weighted average
        for bid in bid_orders:
            self.weight += bid[1]
            self.support_total += bid[0] * bid[1]

        self.support = self.support_total/self.weight

        return self.support

    def calculate_trendline(self, time_points, data_points):
        """
        Calulate resistance trendline by grabbing candlestick data
        """
        self.time_points = time_points
        self.data_points = data_points

        self.trend_line = np.polyfit(self.time_points, self.data_points, 7)

        return self.trend_line

    def calculate_all_trendline(self, candlestick_data):
        """
        Calculate all trendline types (based off binance candlestick data)
        """
        self.trendline_open_equation = self.calculate_trendline(candlestick_data[constants.CANDLESTICK_DATETIME_OPEN], candlestick_data[constants.CANDLESTICK_OPEN])
        self.trendline_close_equation = self.calculate_trendline(candlestick_data[constants.CANDLESTICK_DATETIME_OPEN], candlestick_data[constants.CANDLESTICK_CLOSE])
        self.trendline_high_equation = self.calculate_trendline(candlestick_data[constants.CANDLESTICK_DATETIME_OPEN], candlestick_data[constants.CANDLESTICK_HIGH])
        self.trendline_low_equation = self.calculate_trendline(candlestick_data[constants.CANDLESTICK_DATETIME_OPEN], candlestick_data[constants.CANDLESTICK_LOW])
        self.trendline_volume_equation = self.calculate_trendline(candlestick_data[constants.CANDLESTICK_DATETIME_OPEN], candlestick_data[constants.CANDLESTICK_VOLUME])

    def graph_trendline(self):
        """
        Graphout the trendline
        """
        price = np.poly1d(self.trend_line)

        plt.plot(self.time_points, price(self.time_points), label="trendline")
        plt.draw()
        plt.ioff()
        plt.title("y=%.6fx+%.6f"%(self.trend_line[0],self.trend_line[1])) 
        plt.show()

    def graph_candlesticks(self, dates, open_data, high_data, low_data, close_data):
        """
        Graphout the candlestick
        """
        candlestick_data = [go.Candlestick(
            x=dates,
            open=open_data,
            high=high_data,
            low=low_data,
            close=close_data
        )]
        
        trendline_high_flatten = np.poly1d(self.trendline_high_equation)
        trendline_low_flatten = np.poly1d(self.trendline_low_equation)
        trendline_volume_flatten = np.poly1d(self.trendline_volume_equation)

        trendline_high_data = trendline_high_flatten(dates)
        trendline_low_data = trendline_low_flatten(dates)
        trendline_volume_data = trendline_volume_flatten(dates)

        figure_trendline_high = [go.Scatter(
            x=dates, 
            y=trendline_high_data,
            mode="lines",
            name="High Value trendline"
        )]

        figure_trendline_low = [go.Scatter(
            x=dates,
            y=trendline_low_data,
            mode="lines",
            name="Low Value Trendline"
        )]

        fig = go.Figure(candlestick_data)
        fig.add_traces(figure_trendline_high)
        fig.add_traces(figure_trendline_low)
        fig.show()