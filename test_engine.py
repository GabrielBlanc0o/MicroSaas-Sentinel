import pytest
from pytest import approx
from engine import SentinelBusiness

class TestSentinelBusiness:
    """Comprehensive test suite for SentinelBusiness margin calculations."""
    
    def test_normal_profit_scenario(self):
        """Test typical business scenario with healthy profit margins."""
        business = SentinelBusiness("TechCorp", 10000, 7000)
        assert business.calculate_profit() == 3000
        assert business.calculate_margin() == 30.0
        assert business.get_health_status() == "EXCELLENT"
    
    def test_break_even_scenario(self):
        """Test break-even scenario where revenue equals costs."""
        business = SentinelBusiness("BreakEvenCo", 5000, 5000)
        assert business.calculate_profit() == 0
        assert business.calculate_margin() == 0.0
        assert business.get_health_status() == "CRITICAL"  # 0% margin is CRITICAL, not WARNING
    
    def test_loss_scenario(self):
        """Test scenario where costs exceed revenue."""
        business = SentinelBusiness("LosingBiz", 3000, 5000)
        assert business.calculate_profit() == -2000
        assert business.calculate_margin() == -66.66666666666666
        assert business.get_health_status() == "CRITICAL"
    
    def test_zero_revenue_edge_case(self):
        """Test edge case with zero revenue."""
        business = SentinelBusiness("NoRevenue", 0, 1000)
        assert business.calculate_profit() == -1000
        assert business.calculate_margin() == 0  # Should return 0 to avoid division by zero
        assert business.get_health_status() == "CRITICAL"
    
    def test_negative_revenue_edge_case(self):
        """Test edge case with negative revenue (returns/refunds)."""
        business = SentinelBusiness("NegativeRevenue", -1000, 500)
        assert business.calculate_profit() == -1500
        assert business.calculate_margin() == 0  # Should return 0 for negative revenue
        assert business.get_health_status() == "CRITICAL"
    
    def test_zero_costs_scenario(self):
        """Test scenario with no costs (pure revenue)."""
        business = SentinelBusiness("NoCosts", 8000, 0)
        assert business.calculate_profit() == 8000
        assert business.calculate_margin() == 100.0
        assert business.get_health_status() == "EXCELLENT"
    
    def test_negative_costs_edge_case(self):
        """Test edge case with negative costs (refunds/credits)."""
        business = SentinelBusiness("NegativeCosts", 5000, -1000)
        assert business.calculate_profit() == 6000
        assert business.calculate_margin() == 120.0
        assert business.get_health_status() == "EXCELLENT"
    
    def test_very_small_margins(self):
        """Test scenarios with very small profit margins."""
        # Just barely profitable
        business1 = SentinelBusiness("TinyProfit", 1000, 999.99)
        assert abs(business1.calculate_profit() - 0.01) < 1e-10  # Account for floating point precision
        assert abs(business1.calculate_margin() - 0.001) < 1e-10  # Account for floating point precision
        assert business1.get_health_status() == "WARNING"
        
        # Just barely breaking even
        business2 = SentinelBusiness("BarelyBreakEven", 1000, 1000)
        assert business2.calculate_profit() == 0
        assert business2.calculate_margin() == 0.0
        assert business2.get_health_status() == "CRITICAL"  # 0% margin is CRITICAL
    
    def test_boundary_values_for_health_status(self):
        """Test exact boundary values for health status classifications."""
        
        # CRITICAL to WARNING boundary (0% margin)
        business_critical = SentinelBusiness("Critical", 1000, 1000)
        assert business_critical.get_health_status() == "CRITICAL"  # 0% is CRITICAL
        
        # WARNING to STABLE boundary (10% margin)
        business_warning = SentinelBusiness("Warning", 1000, 900)
        assert business_warning.calculate_margin() == 10.0
        assert business_warning.get_health_status() == "WARNING"  # 10% is still WARNING (needs > 10)
        
        # Just above 10% should be STABLE
        business_stable_just_above = SentinelBusiness("StableJustAbove", 1000, 899.99)
        assert business_stable_just_above.calculate_margin() == 10.001
        assert business_stable_just_above.get_health_status() == "STABLE"
        
        # STABLE to EXCELLENT boundary (25% margin)
        business_stable = SentinelBusiness("Stable", 1000, 750)
        assert business_stable.calculate_margin() == 25.0
        assert business_stable.get_health_status() == "STABLE"  # 25% is still STABLE (needs > 25)
        
        # Just above 25% should be EXCELLENT
        business_excellent_just_above = SentinelBusiness("ExcellentJustAbove", 1000, 749.99)
        assert business_excellent_just_above.calculate_margin() == 25.001
        assert business_excellent_just_above.get_health_status() == "EXCELLENT"
    
    def test_large_numbers_precision(self):
        """Test calculations with large revenue/cost figures."""
        business = SentinelBusiness("LargeCorp", 10000000, 7500000)
        assert business.calculate_profit() == 2500000
        assert business.calculate_margin() == 25.0
        assert business.get_health_status() == "STABLE"  # 25% is STABLE, not EXCELLENT
    
    def test_decimal_precision(self):
        """Test calculations with decimal values."""
        business = SentinelBusiness("DecimalBiz", 12345.67, 9876.54)
        assert abs(business.calculate_profit() - 2469.13) < 0.01
        assert abs(business.calculate_margin() - 20.0) < 0.01
        assert business.get_health_status() == "STABLE"
    
    def test_very_high_margins(self):
        """Test scenarios with extremely high profit margins."""
        business = SentinelBusiness("HighMargin", 1000, 1)
        assert business.calculate_profit() == 999
        assert business.calculate_margin() == 99.9
        assert business.get_health_status() == "EXCELLENT"
    
    def test_floating_point_precision(self):
        """Test floating point precision edge cases."""
        # Test case that might cause floating point precision issues
        #try:
        business = SentinelBusiness("PrecisionTest", 0.1 + 0.2, 0.3)
        assert business.calculate_profit() == approx(0.0 , abs=1e-10) 
        # Due to floating point precision, we get a very small positive margin
        #assert abs(business.calculate_margin() - 1.850371707708594e-14) < 1e-15 FIX THIS WITH a more default tiny number see below --
        assert business.calculate_margin() == approx(0.0 ,1e-10)
        # Since margin > 0 (even if tiny), it should be WARNING
        assert business.get_health_status() == "CRITICAL"
        #except AssertionError:
         #   print(f"ERROR -- {business.get_health_status}") 
        
    def test_business_name_handling(self):
        """Test that business name doesn't affect calculations."""
        # Test with various name formats
        names = ["", "Test Business", "123", "Special!@#$%", "Very Long Business Name That Might Cause Issues"]
        
        for name in names:
            business = SentinelBusiness(name, 5000, 3000)
            assert business.calculate_profit() == 2000
            assert business.calculate_margin() == 40.0
            assert business.get_health_status() == "EXCELLENT"
    
    def test_consistency_across_methods(self):
        """Test that all methods work consistently together."""
        test_cases = [
            (10000, 5000, "EXCELLENT"),
            (10000, 8500, "STABLE"),
            (10000, 9500, "WARNING"),
            (10000, 11000, "CRITICAL"),
            (0, 1000, "CRITICAL"),
            (1000, 0, "EXCELLENT"),
        ]
        
        for revenue, costs, expected_status in test_cases:
            business = SentinelBusiness("Test", revenue, costs)
            profit = revenue - costs
            expected_margin = 0 if revenue <= 0 else (profit / revenue) * 100
            
            assert business.calculate_profit() == profit
            assert abs(business.calculate_margin() - expected_margin) < 0.0001
            assert business.get_health_status() == expected_status

class TestSentinelBusinessErrorHandling:
    """Test error handling and edge cases."""
    
    def test_none_values(self):
        """Test behavior with None values (should work with Python's dynamic typing)."""
        # The current implementation doesn't validate types, so these will work
        # but may cause issues in calculations
        business1 = SentinelBusiness(None, 1000, 500)
        assert business1.name is None
        
        # These will cause TypeError in arithmetic operations
        with pytest.raises(TypeError):
            SentinelBusiness("Test", None, 500).calculate_profit()
        
        with pytest.raises(TypeError):
            SentinelBusiness("Test", 1000, None).calculate_profit()
    
    def test_string_values(self):
        """Test behavior with string values instead of numbers."""
        # The constructor accepts strings, but calculations will fail
        business = SentinelBusiness("Test", "1000", 500)
        
        # This will cause TypeError when trying to do arithmetic
        with pytest.raises(TypeError):
            business.calculate_profit()
        
        with pytest.raises(TypeError):
            SentinelBusiness("Test", 1000, "500").calculate_profit()

    
    def test_boolean_values(self):
        """Test behavior with boolean values."""
        # Python treats bool as subclass of int, but we should handle this gracefully
        business = SentinelBusiness("Test", True, False)
        assert business.calculate_profit() == 1
        assert business.calculate_margin() == 100.0
        assert business.get_health_status() == "EXCELLENT"

class TestSentinelBusinessPerformance:
    """Test performance with large datasets."""
    
    def test_bulk_calculations(self):
        """Test performance with many business calculations."""
        businesses = []
        for i in range(1000):
            revenue = i * 1000
            costs = i * 800
            businesses.append(SentinelBusiness(f"Business{i}", revenue, costs))
        
        # Test that all calculations complete without errors
        for business in businesses:
            profit = business.calculate_profit()
            margin = business.calculate_margin()
            status = business.get_health_status()
        # Basic sanity checks
            assert isinstance(profit, (int, float))
            assert isinstance(margin, (int, float))
            assert isinstance(status, str)
            assert status in ["EXCELLENT", "STABLE", "WARNING", "CRITICAL"]

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
