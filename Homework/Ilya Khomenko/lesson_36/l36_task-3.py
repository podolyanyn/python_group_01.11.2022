import datetime
import requests

weather_token = '1bcbad1cc64b16908f42ea564eaf89ba'

code_to_smile = {
        "Clear": "Ясно \U0001F506",
        "Clouds": "Хмарно \U0001F325",
        "Rain": "Дощ \U0001F326",
        "Drizzle": "Дощ \U0001F326",
        "Thunderstorm": "Гроза \U0001F329",
        "Snow": "Сніг \U0001F328",
        "Mist": "Туман \U0001F32B"
    }
def load_weather():
    try:
        city = input('Enter a city: ')
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_token}&units=metric"
        )
        data = r.json()

        city = data['name']
        cur_weather = data["main"]["temp"]

        weather_desk = data["weather"][0]["main"]
        if weather_desk in code_to_smile:
            wd = code_to_smile[weather_desk]
        else:
            wd = 'Вигляньте в вікно'

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data['wind']["speed"]
        sunrise_stump = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_stump = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        len_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])
        print(f"*****{datetime.datetime.now().strftime('%Y-%m-%d %H-%M')}*****\n"
              f"Погода в місті: {city}\nТемпература: {cur_weather}С°{wd}\n"
              f"Влажність: {humidity}\nТиск: {pressure} мм.рт.ст\nВітер: {wind}\n"
              f"Схід сонця: {sunrise_stump}\nЗахід сонця: {sunset_stump}\nТривалість дня: {len_of_the_day}\n"
              f"*****Гарного дня!*****"
              )
    except:
        print("\U000FEB23 Перевірьте назву міста \U000FEB23")

load_weather()