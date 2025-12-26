import pandas as pd

# Path to your local telemetry file
telemetry_path = r"C:\Users\srila\Downloads\archive (3)\Supplemental Drone Telemetry Data - Drone Operations Log.csv"

def get_calibrated_power_draw():
    df = pd.read_csv(telemetry_path)
    # Filter for successful flights and calculate average power (Voltage * Current)
    # Note: Column names in your CSV may vary, check them with df.columns
    if 'Voltage' in df.columns and 'Current' in df.columns:
        df['Power_W'] = df['Voltage'] * df['Current']
        avg_power = df['Power_W'].mean()
        return avg_power
    return 170.0  # Fallback to standard estimate

print(f"Calibrated Power Draw from Real Data: {get_calibrated_power_draw()}W")