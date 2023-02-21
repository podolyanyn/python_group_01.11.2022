# Robots.txt
# Download and save to file robots.txt from wikipedia, twitter websites etc.

import requests


def get_robots(source):
    request = requests.get(source+'robots.txt')
    source_name = source.split('/')[2]
    with open(f'robots_{source_name}.txt', 'w') as file:
        file.write(request.text)


if __name__ == '__main__':

    urls = ['https://en.wikipedia.org/', 'https://twitter.com/', 'https://beetroot.academy/']
    for url in urls:
        get_robots(url)
