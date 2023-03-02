import datetime
import requests

API_KEY = "84c39b07daeed236b2bfc69f58028884"

url = 'https://api.openweathermap.org/data/2.5/weather'

city = input('Enter the city: ')
params = {'q': city, 'appid': API_KEY, 'units': 'metric', 'lang': 'en'}

response = requests.get(url, params)
data = response.json()

main = data['weather'][0]['main']
description = data['weather'][0]['description']
temp = data['main']['temp']
pressure = data['main']['pressure']
humidity = data['main']['humidity']
wind = data['wind']['speed']
sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S')
sunset = datetime.datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S')

output = f"""The weather in {city}:
{main}, {description}
Temperature - {temp}°C
Humidity    - {humidity}%
Wind        - {wind} m/s
Sunrise     - {sunrise}
Sunset      - {sunset}"""

print(output)
