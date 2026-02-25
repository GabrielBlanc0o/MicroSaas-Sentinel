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
        margin = (self.calculate_profit() / self.revenue) * 100

        # avoid floating point noise close to 0 (e.g., 1e-14)
        eps = 1e-9
        if -eps < margin < eps:
            return 0.0

        return margin

    def get_health_status(self):
        margin = self.calculate_margin()
        try:
            if margin > 25:
                return "EXCELLENT"
            elif margin > 10:
                return "STABLE"
            elif margin > 0:
                return "WARNING"
            else:
                return "CRITICAL"
        except AssertionError:
            return "ERROR TEST PRECISION EN UN PUNTO FLOTANTE RANGO  test_engine.py::TestSentinelBusiness::test_floating_point_precision "
            