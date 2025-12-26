import pandas as pd
import random

def generate_drone_maintenance_logs(n=100):
    data = {
        "Log_ID": [f"MNT-{i}" for i in range(n)],
        "Component": [random.choice(["Motor", "Battery", "Propeller", "ESC"]) for _ in range(n)],
        "Hours_Used": [random.randint(10, 200) for _ in range(n)],
        "Status": [random.choice(["Good", "Requires Service", "Critical"]) for _ in range(n)]
    }
    df = pd.DataFrame(data)
    df.to_csv("data/synthetic/maintenance_logs.csv", index=False)
    print("✅ Synthetic Maintenance logs generated in data/synthetic/")

if __name__ == "__main__":
    generate_drone_maintenance_logs()