"""
Robots.txt
Download and save to file robots.txt from wikipedia, twitter websites etc.
"""
import requests


def download_robots_txt(url):
    # Get the root URL for the given website
    # example: 'https://twitter.com/i/bookmarks' -> twitter.com
    root_url = url.split("//")[1].split("/")[0]

    robots_url = f'https://{root_url}/robots.txt'
    resp = requests.get(robots_url)

    if resp.status_code == 200:
        with open(f'{root_url}_robots.txt', 'w') as f:
            f.write(resp.text)
    else:
        print('Something went wrong. Check URL')


if __name__ == '__main__':
    urls = ['https://en.wikipedia.org', 'https://twitter.com', 'https://www.reddit.com/r/HIMYM/']
    for url in urls:
        download_robots_txt(url)
