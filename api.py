import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_key = os.getenv("WEATHER_API_KEY")
#print(repr(API_key))

def Get_location(city_name,state_code):
    try:
        location =  requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code}&appid={API_key}")
        location.raise_for_status()
        data = location.json()
        #print(data)
        return data
    except requests.exceptions.Timeout:
        print("timed out")
        return None
    except requests.exceptions.RequestException as e:
        print("Request faialed",e)
        return None


def get_weather_for_location(city, state):
    try:
        w_city = city
        w_state = state
        loc_data = Get_location(w_city,w_state)
        lat = loc_data[0]["lat"]
        lon = loc_data[0]["lon"]
        response = requests.get(
        url=f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}"
    
    )
        response.raise_for_status()
        data = response.json()
        print(f"The temperature today is {data['main']['temp']}")
        print(f"The min and max today is {data['main']['temp_min']} - {data['main']['temp_max']}")
        print(f"It feels like {data['main']['feels_like']}")
    except requests.exceptions.RequestException as e:
        print("something went wrong",e)
        


