import pandas as pd
import os

# PDF Page 5 Requirement: Use the internal repository structure
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
STARTUP_PATH = os.path.join(BASE_DIR, "data", "raw", "Listofstartups.csv")
TELEMETRY_PATH = os.path.join(BASE_DIR, "data", "raw", "Supplemental Drone Telemetry Data - Drone Operations Log.csv")

def get_connected_data():
    """
    Requirement: Data Preprocessing Pipeline.
    This function reads the raw CSVs and returns cleaned, validated data.
    """
    results = {"telemetry": {}, "startups": [], "status": "Error"}
    
    try:
        # 1. Process Telemetry (Drone Logs)
        if os.path.exists(TELEMETRY_PATH):
            tel_df = pd.read_csv(TELEMETRY_PATH)
            # Cleanup: Convert to numeric and calculate averages
            avg_flight = pd.to_numeric(tel_df['Flight Duration (minutes)'], errors='coerce').mean()
            avg_payload = pd.to_numeric(tel_df['Actual Carry Weight (kg)'], errors='coerce').mean()
            results["telemetry"] = {
                "avg_flight_time_mins": round(avg_flight, 2),
                "avg_payload_kg": round(avg_payload, 2),
                "total_records": len(tel_df)
            }

        # 2. Process Startups (India Ecosystem)
        if os.path.exists(STARTUP_PATH):
            # Requirement: Handle 'Saw 23 fields' error on line 28
            sta_df = pd.read_csv(STARTUP_PATH, on_bad_lines='skip')
            # Filter for Drone startups in India
            drone_firms = sta_df[sta_df['Sector'].str.contains('Drone|Aerospace', case=False, na=False)]
            results["startups"] = drone_firms['Name of the startup'].head(5).tolist()
            
        results["status"] = "Successfully Connected"
        
    except Exception as e:
        results["status"] = f"Connection Error: {str(e)}"
        
    return results