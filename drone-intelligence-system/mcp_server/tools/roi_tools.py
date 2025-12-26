def calculate_drone_roi(initial_investment, daily_operational_cost, manual_labor_cost_replaced, revenue_per_day):
    """
    Calculates ROI and Break-even for Indian drone operations.
    """
    # Net daily gain = (Replaced Labor Cost + Daily Revenue) - Operational Cost
    daily_net_gain = (manual_labor_cost_replaced + revenue_per_day) - daily_operational_cost
    
    if daily_net_gain <= 0:
        return {"error": "Operation is not profitable with current parameters."}
    
    break_even_days = initial_investment / daily_net_gain
    annual_roi = ((daily_net_gain * 365) / initial_investment) * 100
    
    return {
        "break_even_days": round(break_even_days, 2),
        "annual_roi_percent": round(annual_roi, 2),
        "recommendation": "High Viability" if annual_roi > 50 else "Moderate Viability"
    }