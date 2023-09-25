import requests
import os
from dotenv import load_dotenv
load_dotenv()

def get_weather(location = "Rajshahi"):     # default city is Raj
    api_key = os.getenv("WEATHER_API_KEY")  # openWeather API
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        return f"The temperature in {location} is {temperature} degrees Celsius and the weather is {description}."
    else:
        return "Sorry, I couldn't get the weather information. Please try again later."