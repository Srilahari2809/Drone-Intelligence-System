import requests

BASE_URL = "http://127.0.0.1:8000"

def test_data_connection():
    """Test if the CSV files are being read correctly."""
    response = requests.get(f"{BASE_URL}/insights")
    assert response.status_code == 200
    data = response.json()
    assert "telemetry" in data
    print("✅ Data Connection Test Passed")

def test_roi_calculation():
    """Test the POST calculation tool."""
    payload = {"investment": 1000, "revenue": 1500}
    response = requests.post(f"{BASE_URL}/calculate-roi", json=payload)
    assert response.status_code == 200
    assert response.json()["estimated_profit"] == 500
    print("✅ ROI Calculation Test Passed")

if __name__ == "__main__":
    test_data_connection()
    test_roi_calculation()