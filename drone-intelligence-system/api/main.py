from fastapi import FastAPI
from api.routes import calculate  # Ensure your routes are imported

# This is the line uvicorn is looking for!
app = FastAPI(title="Drone Intelligence System")

# Include your routers
app.include_router(calculate.router, prefix="/calculate")

@app.get("/")
async def root():
    return {"message": "Drone Intelligence API is running"}