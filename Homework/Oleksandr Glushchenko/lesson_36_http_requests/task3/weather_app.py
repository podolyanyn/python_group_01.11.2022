"""
The Weather app
Write a console application which takes as an input a city name and returns current weather in the format
of your choice.
For the current task, you can choose any weather API or website or use openweathermap.org
"""
import requests


def get_current_weather(city: str):

    # openweathermap API documentation
    # https://openweathermap.org/current

    api_key = 'e60cab685a794d53240c9f9690b23026'
    api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    resp = requests.get(api_url)

    if resp.status_code == 200:
        data = resp.json()
        weather = data['weather'][0]['description']
        humidity = data['main']['humidity']
        temperature = data['main']['temp']
        wind_speed = data['wind']['speed']

        return f'The weather in {city} is {weather} with a temperature of {temperature} degrees Celsius' \
               f' humidity of {humidity}%, and wind speed of {wind_speed} m/s'
    else:
        return f'Error getting data. Please check spelling of the city: "{city}". ' \
               f'Response status code: {resp.status_code}'


if __name__ == '__main__':
    c = input("Enter city name: ")
    print(get_current_weather(c))
