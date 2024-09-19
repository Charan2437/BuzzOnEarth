from fastapi import FastAPI, HTTPException
import pandas as pd

app = FastAPI()

# Load the data from the CSV file (you can adjust this to the correct file path)
data = pd.read_csv('data/all_city_data_with_pop.csv')

# Clean the dataset (optional, based on the structure)
data = data[['geometry', 'EV_stations', 'city']]

@app.get("/ev-stations/{city}")
async def get_ev_stations(city: str):
    # Filter data by city name
    city_data = data[(data['city'].str.lower() == city.lower()) & (data['EV_stations'] == 1)]
    
    if city_data.empty:
        raise HTTPException(status_code=404, detail="City not found")
    
    # Prepare response with EV station locations and count
    response = city_data.to_dict(orient="records")
    
    return response

# To run: `uvicorn main:app --reload`
