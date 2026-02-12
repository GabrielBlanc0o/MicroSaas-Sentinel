def calculate_business_health(revenue, costs):
    """
    Basic logic to determine if a business is healthy.
    """
    net_profit = revenue - costs
    margin = (net_profit / revenue) * 100 if revenue > 0 else 0
    
    return {
        "profit": net_profit,
        "margin_percentage": f"{margin:.2f}%",
        "is_healthy": net_profit > 0
    }

# Simulation for a real-world case (Random Business)
monthly_revenue = 5000
monthly_operating_costs = 3200

report = calculate_business_health(monthly_revenue, monthly_operating_costs)

print(f"--- Sentinel Financial Report ---")
print(f"Net Profit: ${report['profit']}")
print(f"Profit Margin: {report['margin_percentage']}")
print(f"Health Status: {'✅ Solid' if report['is_healthy'] else '⚠️ Warning'}")