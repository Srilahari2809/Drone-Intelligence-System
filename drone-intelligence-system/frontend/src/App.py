import streamlit as st
import requests

# MUST BE THE FIRST COMMAND
st.set_page_config(page_title="Drone Intelligence Dashboard", layout="wide")

st.title("🚁 Drone Intelligence Dashboard")

# Navigation Sidebar
page = st.sidebar.radio("Navigate", ["Industry Insights", "ROI Tool", "AI Drone Advisor"])

if page == "Industry Insights":
    st.header("📊 Market Data: Indian Drone Ecosystem")
    st.write("Browse certified drone manufacturers and service providers in India.")
    
    if st.button("Fetch Company List"):
        try:
            # Connect to backend endpoint
            res = requests.get("http://127.0.0.1:8000/calculate/insights")
            
            if res.status_code == 200:
                result = res.json()
                if result["status"] == "success":
                    st.success(f"Retrieved {result['count']} Companies!")
                    
                    # Display the full table from listofcompanies.csv (Phase 6)
                    st.dataframe(
                        result["data"], 
                        use_container_width=True,
                        column_config={
                            "Company Name": st.column_config.TextColumn("Company"),
                            "Primary Category": "Category",
                            "HQ / Location": "Location"
                        }
                    )
                else:
                    st.error(f"Data Error: {result['message']}")
            else:
                st.error(f"Server Error {res.status_code}. Check if backend is running.")
        except Exception as e:
            st.error(f"Connection error: {e}")

elif page == "ROI Tool":
    st.header("💰 Business ROI Predictor")
    inv = st.number_input("Investment (INR)", value=100000)
    rev = st.number_input("Revenue (INR)", value=150000)
    if st.button("Calculate"):
        try:
            payload = {"investment": inv, "revenue": rev}
            res = requests.post("http://127.0.0.1:8000/calculate/calculate-roi", json=payload)
            st.success(f"Estimated Profit: ₹{res.json().get('profit', 'N/A')}")
        except:
            st.error("Could not calculate. Is the backend running?")

elif page == "AI Drone Advisor":
    st.header("🤖 AI Drone Selection Assistant")
    needs = st.text_input("What is your drone use case? (e.g., crops, delivery)")
    
    if st.button("Get Suggestion"):
        if needs:
            query = needs.lower()
            if any(x in query for x in ["crop", "farm", "agriculture"]):
                st.info("### Recommendation: IoTechWorld Agribot")
                st.write("Specialized for Indian agriculture with high payload for spraying.")
            elif any(x in query for x in ["film", "video", "wedding"]):
                st.info("### Recommendation: DJI Mavic 3 Pro")
                st.write("Best-in-class camera for cinematic Indian weddings.")
            else:
                st.write("Based on your need, I recommend checking the **Industry Insights** tab for local vendors.")