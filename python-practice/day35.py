# Question: Day 35: Implement a simple REST API consumer using requests module.
import requests

def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': 'YOUR_API_KEY',
        'units': 'metric'
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        return f"{data['name']}: {data['main']['temp']}°C"
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

print(get_weather('London'))
