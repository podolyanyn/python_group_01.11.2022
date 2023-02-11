import requests

url = "https://en.wikipedia.org/robots.txt"
response = requests.get(url)
with open('Robots_wiki.txt', 'w', encoding="utf-8") as file:
    file.write(response.text)

url = "https://twitter.com/robots.txt"
response = requests.get(url)
with open('Robots_twitter.txt', 'w', encoding="utf-8") as file:
    file.write(response.text)
