import pandas as pd
import os

def verify():
    print("--- Dataset Connectivity Report ---")
    
    # 1. Startups Connection
    try:
        # Using latin1 to handle special characters (Requirement: Phase 1 Research)
        df_s = pd.read_csv('data/raw/Listofstartups.csv', encoding='latin1', on_bad_lines='skip')
        print(f"✅ Startup Dataset: CONNECTED ({len(df_s)} rows)")
    except Exception as e:
        print(f"❌ Startup Dataset ERROR: {e}")

    # 2. Telemetry Connection
    try:
        # skipping bad lines handles the error on line 28 (Requirement: Phase 2 Preprocessing)
        df_t = pd.read_csv('data/raw/Supplemental Drone Telemetry Data - Drone Operations Log.csv', on_bad_lines='skip')
        print(f"✅ Telemetry Dataset: CONNECTED ({len(df_t)} rows)")
    except Exception as e:
        print(f"❌ Telemetry Dataset ERROR: {e}")

if __name__ == "__main__":
    verify()