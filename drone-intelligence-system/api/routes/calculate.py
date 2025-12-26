import pandas as pd
from fastapi import APIRouter

router = APIRouter()

@router.get("/insights")
async def get_drone_insights():
    try:
        # Load the uploaded file with specific encoding for Indian characters
        df = pd.read_csv("data/raw/listofcompanies.csv", encoding='latin1')
        
        # Convert the dataframe to a list of dictionaries for the API
        companies_data = df.to_dict(orient="records")
        
        return {
            "status": "success",
            "count": len(companies_data),
            "data": companies_data
        }
    except Exception as e:
        return {"status": "error", "message": f"Failed to read CSV: {str(e)}"}