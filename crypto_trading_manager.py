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

    def calculate_rsi(self, candlestick_data):
        """
        Calculate rsi
        """
        self.change_up = []
        self.change_down = []

        for candlestick in candlestick_data:
            # if candlestick[constants.CANDLESTICK_OPEN] > candlestick[constants.CANDLESTICK_CLOSE]:
            #     change_up.append(candlestick[constants.CANDLESTICK_OPEN] - candlestick[constants.CANDLESTICK_CLOSE])
            #     change_down.append(0)
            # else:
            #     change_up.append(0)
            #     change_down.append(candlestick[constants.CANDLESTICK_OPEN] - candlestick[constants.CANDLESTICK_CLOSE])
            if candlestick[1] == candlestick[4]:
                self.change_up.append(0)
                self.change_down.append(0)
                pass
            elif candlestick[1] > candlestick[4]:
                self.change_up.append(candlestick[1] - candlestick[4])
                self.change_down.append(0)
            else:
                self.change_up.append(0)
                self.change_down.append(candlestick[4] - candlestick[1])

        self.change_up_avg = np.average(self.change_up)
        self.change_down_avg = np.average(self.change_down)

        self.rs_value = (self.change_up_avg/self.change_down_avg)
        self.rsi = (100 - (100/(1 + self.rs_value)))
        return self.rsi

    def localize_rsi_to_coin(self, candlestick_data):
        """
        Get the rsi value in terms of the coin
        """
        self.max_rsi = 0
        self.min_rsi = 999999

        for candlestick in candlestick_data:
            # if candlestick[constants.CANDLESTICK_OPEN] > candlestick[constants.CANDLESTICK_CLOSE]:
            #     change_up.append(candlestick[constants.CANDLESTICK_OPEN] - candlestick[constants.CANDLESTICK_CLOSE])
            #     change_down.append(0)
            # else:
            #     change_up.append(0)
            #     change_down.append(candlestick[constants.CANDLESTICK_OPEN] - candlestick[constants.CANDLESTICK_CLOSE])
            if self.max_rsi < candlestick[2]:
                self.max_rsi = candlestick[2]
            
            if self.min_rsi > candlestick[3]:
                self.min_rsi = candlestick[3]
        
        self.rsi_to_coin = self.min_rsi + (self.max_rsi - self.min_rsi) * (self.rsi/100)
        return self.rsi_to_coin

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
        
        # trendline_high_flatten = np.poly1d(self.trendline_high_equation)
        # trendline_low_flatten = np.poly1d(self.trendline_low_equation)
        # trendline_volume_flatten = np.poly1d(self.trendline_volume_equation)

        # trendline_high_data = trendline_high_flatten(dates)
        # trendline_low_data = trendline_low_flatten(dates)
        # trendline_volume_data = trendline_volume_flatten(dates)

        # figure_trendline_high = [go.Scatter(
        #     x=dates, 
        #     y=trendline_high_data,
        #     mode="lines",
        #     name="High Value trendline"
        # )]

        # figure_trendline_low = [go.Scatter(
        #     x=dates,
        #     y=trendline_low_data,
        #     mode="lines",
        #     name="Low Value Trendline"
        # )]
        
        print(dates.size)
        rsi_line = [self.rsi_to_coin] * dates.size

        figure_rsi_line = [go.Scatter(
            x=dates,
            y=rsi_line,
            mode="lines",
            name="RSI line"
        )]

        fig = go.Figure(candlestick_data)
        # fig.add_traces(figure_trendline_high)
        # fig.add_traces(figure_trendline_low)
        fig.add_traces(figure_rsi_line)
        fig.show()