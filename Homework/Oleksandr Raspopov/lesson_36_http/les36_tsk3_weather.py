# The Weather app
# Write a console application which takes as an input a city name and returns current weather in the format of your choice.
# For the current task, you can choose any weather API or website or use openweathermap.org

import requests

KEY = "5fdd472908385dc9e4ee0706958a2a6e"


def get_weather(lat, lon):
    api_call = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={KEY}"
    request = requests.get(api_call).json()
    weather = request["weather"][0]["description"]
    temp = request["main"]["temp"]
    temp_cels = round((int(temp) - 273.15), 2)
    humidity = request["main"]["humidity"]
    wind = request["wind"]["speed"]
    city, country = request["name"], request["sys"]["country"]
    print(f'{city}, {country}\n'
          f'weather: {weather}\n'
          f'temp C: {temp_cels}\n'
          f'humidity: {humidity}\n'
          f'wind: {wind}\n')


def coordinates_by_name(name, country="UA", limit=1):
    api_call = f"http://api.openweathermap.org/geo/1.0/direct?q={name},{country}&limit={limit}&appid={KEY}"
    request = requests.get(api_call).json()
    lat = request[0]["lat"]
    lon = request[0]["lon"]
    return lat, lon


def main():
    city = input('Enter <city>: ')
    country = input('Enter <country code>: ')
    try:
        lat, lon = coordinates_by_name(city, country)
        return get_weather(lat, lon)
    except IndexError:
        print(f'Not found\n')
        return main()


if __name__ == '__main__':
    while True:
        main()
