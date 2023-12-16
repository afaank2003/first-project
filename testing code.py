# Rain forecaster
# Enter latitude and longitude in this format: 39.7456,-97.0892
import requests

def fetch_weather_data():
    
    latitude = input("Enter latitude: ")
    longitude = input("Enter longitude: ")

    # URL for the /points endpoint
    url = f"https://api.weather.gov/points/{latitude},{longitude}"

    # Making the API request 
    response = requests.get(url)
    forecast_url = response.json()['properties']['forecastHourly']

    # Fetching the hourly forecast data
    forecast_response = requests.get(forecast_url)
    forecast_data = forecast_response.json()['properties']['periods']

    return forecast_data

# Getting weather data (Placeholder for the fetch_weather_data function)
weather_forecasts = fetch_weather_data()

# Initializing an empty list to store selected forecasts
selected_forecasts = []

# Counter for the while loop
counter = 0

# While loop that continues until a rain forecast is reached
while counter < len(weather_forecasts):
    forecast = weather_forecasts[counter]['shortForecast']
    
    # Check if the forecast includes rain
    if 'rain' in forecast.lower():
        print(f"Rain forecast reached: {forecast}")
        break

    counter += 1

# Note: The loop stops when it encounters the first rain forecast

