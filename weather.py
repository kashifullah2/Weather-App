from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import requests
from datetime import datetime
import pytz

#Api get from openweathermap if not working update the api
api_key = "YOUR api KEY"
class Weather:

    def __init__(self, city):
        self.city = city
        self.api_key = api_key
        self.geolocator = Nominatim(user_agent="weather_forecasting_app_v1.0")
        self.location = self.geolocator.geocode(city)
        
        if self.location is None:
            raise ValueError(f"Could not find location for '{city}'. Please enter a valid city name.")
            
        self.timezone_finder = TimezoneFinder()
        self.timezone = self.timezone_finder.timezone_at(lng=self.location.longitude, lat=self.location.latitude)

        self.long_lat = f"{round(self.location.latitude)}°N,{round(self.location.longitude,4)}°E"
        # Using the onecall API endpoint as in your original code
        self.api = f"https://api.openweathermap.org/data/2.5/onecall?lat={self.location.latitude}&lon={self.location.longitude}&units=metric&exclude=hourly&appid={self.api_key}"
        self.home = pytz.timezone(self.timezone)
        self.local_time = datetime.now(self.home)
        self.current_time = self.local_time.strftime("%I:%M:%p")

        try:
            self.json_data = requests.get(self.api).json()
            
            # Check if 'current' exists in the response
            if 'current' not in self.json_data:
                # If not, use the alternative API endpoint as a fallback
                alt_api = f"https://api.openweathermap.org/data/2.5/weather?lat={self.location.latitude}&lon={self.location.longitude}&units=metric&appid={self.api_key}"
                self.json_data = requests.get(alt_api).json()
                
                # Map the different structure to match what we expect
                self.temperature = self.json_data["main"]["temp"]
                self.humidity = self.json_data["main"]["humidity"]
                self.pressure = self.json_data["main"]["pressure"]
                self.wind_speed = self.json_data["wind"]["speed"]
                self.weather_description = self.json_data["weather"][0]["description"]
            else:
                # Original structure works
                self.temperature = self.json_data["current"]["temp"]
                self.humidity = self.json_data["current"]["humidity"]
                self.pressure = self.json_data["current"]["pressure"]
                self.wind_speed = self.json_data["current"]["wind_speed"]
                self.weather_description = self.json_data["current"]["weather"][0]["description"]
                
        except Exception as e:
            raise Exception(f"Error fetching weather data: {str(e)}")

    def __repr__(self):
        return f"Current Time: {self.current_time}\nTimezone: {self.timezone}\nTemperature: {self.temperature}\nHumidity: {self.humidity}\nPressure: {self.pressure}\nWind Speed: {self.wind_speed}\nDescription: {self.weather_description}"