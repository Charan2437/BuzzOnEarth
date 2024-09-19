from fastapi import FastAPI, HTTPException
import pandas as pd

app = FastAPI()

# Load the data from the CSV file (adjust to the correct file path)
data = pd.read_csv('data/all_city_data_with_pop.csv')
data = data[['geometry','parking','edges','EV_stations','parking_space','civic','restaurant','park','school','node','Community_centre','place_of_worship','university','cinema','library','commercial','retail','townhall','government','residential','city','population']]

# Add relevant columns, convert population to int (or string if needed)
data['population'] = data['population'].fillna(0).astype(str)  # Handling NaNs and converting to str


# Example usages:
# http://127.0.0.1:8000/parking/city_name
# http://127.0.0.1:8000/edges/city_name
# http://127.0.0.1:8000/EV_stations/city_name
# http://127.0.0.1:8000/parking_space/city_name
# http://127.0.0.1:8000/civic/city_name
# http://127.0.0.1:8000/restaurant/city_name
# http://127.0.0.1:8000/park/city_name
# http://127.0.0.1:8000/school/city_name
# http://127.0.0.1:8000/node/city_name
# http://127.0.0.1:8000/Community_centre/city_name
# http://127.0.0.1:8000/place_of_worship/city_name
# http://127.0.0.1:8000/university/city_name
# http://127.0.0.1:8000/cinema/city_name
# http://127.0.0.1:8000/townhall/city_name
# http://127.0.0.1:8000/retail/city_name
# http://127.0.0.1:8000/commercial/city_name
# http://127.0.0.1:8000/library/city_name
# http://127.0.0.1:8000/population/city_name
# http://127.0.0.1:8000/residential/city_name
# http://127.0.0.1:8000/government/city_name

# city_name = ['Frankfurt', 'Munich', 'Kaiserslautern', 'Saarbrucken', 'Stuttgart', 'karlsruhe', 'Trier', 'Mainz', 'Berlin']

@app.get("/{entity}/{city}")
async def get_ev_stations(entity:str, city: str):
    # Filter data by city name
    city_data = data[(data['city'].str.lower() == city.lower()) & (data[entity] > 0)]
    city_data = city_data[['geometry',entity]]
    
    if city_data.empty:
        raise HTTPException(status_code=404, detail="City not found")
    
    # Prepare response with EV station locations and count, including population as int
    response = city_data.to_dict(orient="records")
    
    return response
