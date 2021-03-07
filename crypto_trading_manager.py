import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go


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

    def calculate_trendline(self, time_points, data_points, line_type="straight"):
        """
        Calulate resistance trendline by grabbing candlestick data
        """
        self.time_points = time_points
        self.data_points = data_points

        self.trend_line = np.polyfit(self.time_points, self.data_points, 1)

        return self.trend_line

    def graph_trendline(self):
        """
        Graphout the trendline
        """
        price = np.poly1d(self.trend_line)

        plt.plot(self.time_points, price(self.time_points), label="trendline")
        # plt.plot(self.time_points, self.data_points, label="high points")
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

        fig = go.Figure(candlestick_data)
        fig.show()