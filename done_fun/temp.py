import requests
import json
from Head.Mouth import *

def get_temperature_openweathermap(city):
    api_key = "b097461059e3563bffa3f97178f651db"
    web = "https://api.openweathermap.org/data/2.5/weather"

    response = requests.get(web, params={"q": city, "appid": api_key,"units": "metric"})

    if response.status_code == 200:
        data = json.loads(response.text)
        if 'main' in data:
            temperature_celsius = data["main"]["temp"]
            return temperature_celsius
        else:
            print("Error: 'main' key not found in API response")
    else:
        print(f"Error: Failed to fetch data from API. Status code: {response.status_code}")

    return None


def Temp():
    city = "anand"

    temperature_celsius = get_temperature_openweathermap(city)

    if temperature_celsius is not None:
        speak(f"The weather in {city} is {temperature_celsius}°C")
    else:
        print("Temperature data not available.")
