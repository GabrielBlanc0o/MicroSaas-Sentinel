class SentinelBusiness:
    def __init__(self, name, revenue, costs):
        self.name = name
        self.revenue = revenue
        self.costs = costs

    def calculate_profit(self):
        return self.revenue - self.costs

    def calculate_margin(self):
        # validate division with 0
        if self.revenue <= 0:
            return 0
        # ecuation
        return (self.calculate_profit() / self.revenue) * 100

    def get_health_status(self):
        margin = self.calculate_margin()
        if margin > 25:
            return "EXCELLENT"
        elif margin > 10:
            return "STABLE"
        elif margin > 0:
            return "WARNING"
        else:
            return "CRITICAL"