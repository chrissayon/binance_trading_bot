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