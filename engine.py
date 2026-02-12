class SentinelBusiness():
    def __init__(self,name,revenue,costs): # Not negative numbers
        self.name = name
        self.revenue = revenue
        self.costs = costs
        
        if costs < 0:
           yield (costs,False)

    def  calculate_profit(self):
        return self.revenue - self.costs
     
    def calculte_margin(self): # margin = (revenue - costs / revenue) x 100
        if self.revenue < 0 :
            return 0
        return (self.calculate_profit() - self.revenue) * 100
   
        def get_healt_status(self): # return status
            margin = self.calculate_margin()
            if margin > 25:
                return "EXCELLENT"
            elif margin > 10:
                return "STABLE"
            elif margin > 0:
                return "WARNING"
            else:
                return "CRITICAL"
    
