# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 10:58:04 2024

@author: chien 
"""
import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_current_weather():
  while True:
    print(f"\n*** Get Current Weather Conditions ***\n")
    
    city = input("\nPlease enter a city name:\n")
    
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
    
    # print(request_url)
    
    weather_data = requests.get(request_url).json()
    
    
    # print(weather_data)
    pprint(weather_data)
   
   
    pprint(f'Current weather for {weather_data["name"]}:')
    pprint(f'The temp is {weather_data["main"]["temp"]:.1f}°')
    pprint(f'The humidity is {weather_data["main"]["humidity"]}%')
    pprint(f'The wind speed is {weather_data["wind"]["speed"]}km/h')
    pprint(
        f'{weather_data["weather"][0]["description"].capitalize()} and feels like {weather_data["main"]["feels_like"]:.1f}°\n')
    
    pprint(
        f'The high today is {weather_data["main"]["temp_max"]:.1f}° and the low is {weather_data["main"]["temp_min"]:.1f}°\n')

    # Check for rain data
    if "rain" in weather_data:
        rain_1h = weather_data["rain"].get("1h", 0)
        rain_3h = weather_data["rain"].get("3h", 0)
        pprint(f'Rain volume for the last 1 hour: {rain_1h} mm')
        pprint(f'Rain volume for the last 3 hours: {rain_3h} mm')
    else:
        pprint('No rain data available.')
        
    print(f'\n\n*** End of Current Weather Conditions ***\n\n')

    another_city = input("\nWould you like to check the weather for another city? (yes/no)\n")
    if another_city.lower() != 'yes':
        break
    


if __name__ == "__main__":
    get_current_weather()
    
   







