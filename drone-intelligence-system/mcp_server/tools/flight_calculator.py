def estimate_flight_time(battery_capacity_mah, battery_voltage, drone_weight_kg, payload_weight_kg):
    """
    Calculates estimated flight time using the 80% safe discharge rule.
    """
    # Total weight (All-Up Weight)
    auw = drone_weight_kg + payload_weight_kg
    
    # Energy in Watt-hours (Wh) = (mAh * V) / 1000
    energy_wh = (battery_capacity_mah * battery_voltage) / 1000
    
    # Average power consumption (Estimate: 170W per 1kg of AUW for hovering)
    avg_power_watts = auw * 170 
    
    # 80% discharge safety margin
    safe_energy_wh = energy_wh * 0.8 
    
    flight_time_hours = safe_energy_wh / avg_power_watts
    flight_time_minutes = flight_time_hours * 60
    
    return {
        "estimated_hover_time_min": round(flight_time_minutes, 2),
        "safety_margin": "80% (Reserve Kept)",
        "all_up_weight_kg": auw
    }