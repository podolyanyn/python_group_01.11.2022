import requests, json, customtkinter, time


start = time.perf_counter()
# task_1


# def get_site_name(text):
#     site_name = text.split('/')[2]
#     return site_name
#
#
# urls = [
#     "https://en.wikipedia.org/robots.txt",
#     "https://www.reddit.com/robots.txt",
#     "https://twitter.com/robots.txt",
#     "https://www.youtube.com/robots.txt",
#     "https://www.google.com/robots.txt",
#     "https://www.instagram.com/robots.txt"
# ]
#
# for url in urls:
#     r = requests.get(url, stream=True)
#     with open(f"robots_{get_site_name(url)}.txt", 'wb') as fd:
#         for chunk in r.iter_content(chunk_size=128):
#             fd.write(chunk)

# task_2

payload = {'subreddit': 'Python'}
url = "https://api.pushshift.io/reddit/comment/search/"


def get_comments(url, payload):
    r = requests.get(url, params=payload)
    comments = []
    time = []
    for data in range(len(r.json()["data"])):
        comment = r.json()["data"][data]["body"]
        date = r.json()["data"][data]["utc_datetime_str"]
        comments.append(comment)
        time.append(date)

    my_dict = {keys: values for (keys, values) in zip(time, comments)}
    sorted_dict = {keys: values for keys, values in sorted(my_dict.items())}

# for key, value in sortedDict.items():
    with open("comments.json", "w") as com:
        json.dump(sorted_dict, com, indent=2)


get_comments(url, payload)
finish = time.perf_counter()
print(str(finish-start))

# task_3 Трішки загрався з одним GUI з цього відео https://www.youtube.com/watch?v=iM3kjbbKHQU


# def find_weather(entry, temperature_label, pressure_label, humidity_label, description_label):
#     api_key = "36abbec460d435433e52d08e3defe4a3"
#     base_url = "https://api.openweathermap.org/data/2.5/weather?"
#
#     city_name = entry.get()
#
#     complete_url = base_url + "appid=" + api_key + "&q=" + city_name
#
#     response = requests.get(complete_url)
#
#     x = response.json()
#
#     if x["cod"] != "404":
#         y = x["main"]
#         current_temperature = y["temp"]
#         current_pressure = y["pressure"]
#         current_humidity = y["humidity"]
#         z = x["weather"]
#         weather_description = z[0]["description"]
#
#         temperature_label.configure(text="Temperature: " + str(round(current_temperature-273.15)) + " C")
#         pressure_label.configure(text="Pressure: " + str(current_pressure) + " hPa")
#         humidity_label.configure(text="Humidity: " + str(current_humidity) + " %")
#         description_label.configure(text="Description: " + weather_description)
#     else:
#         temperature_label.configure(text="City not found")
#         pressure_label.configure(text="")
#         humidity_label.configure(text="")
#         description_label.configure(text="")
#
#
# customtkinter.set_appearance_mode("dark")
# customtkinter.set_default_color_theme("dark-blue")
#
# root = customtkinter.CTk()
# root.geometry("500x350")
#
# frame = customtkinter.CTkFrame(master=root)
# frame.pack(pady=20, padx=20, fill="both", expand=True)
#
# label = customtkinter.CTkLabel(master=frame, text="Weather Today", font=("Roboto", 24))
# label.pack(pady=12, padx=10)
#
# entry = customtkinter.CTkEntry(master=frame, placeholder_text="City Name")
# entry.pack(pady=12, padx=10)
#
# temperature_label = customtkinter.CTkLabel(master=frame, text="")
# temperature_label.pack(pady=5, padx=10)
#
# pressure_label = customtkinter.CTkLabel(master=frame, text="")
# pressure_label.pack(pady=5, padx=10)
#
# humidity_label = customtkinter.CTkLabel(master=frame, text="")
# humidity_label.pack(pady=5, padx=10)
#
# description_label = customtkinter.CTkLabel(master=frame, text="")
# description_label.pack(pady=5, padx=10)
#
# button = customtkinter.CTkButton(master=frame, text="Find", command=lambda: find_weather(
#     entry,
#     temperature_label,
#     pressure_label,
#     humidity_label,
#     description_label
# ))
# button.pack(pady=12, padx=10)
#
# root.mainloop()

