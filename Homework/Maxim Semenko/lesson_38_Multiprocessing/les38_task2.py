import requests
import datetime
import json
from concurrent.futures import ProcessPoolExecutor


params = [{'subreddit': 'Ukraine', 'sort-type': 'created_utc'},
          {'subreddit': 'USA', 'sort-type': 'created_utc'},
          {'subreddit': 'Python', 'sort-type': 'created_utc'}]


def download_comments(params):
    url = "https://api.pushshift.io/reddit/comment/search/"
    response = requests.get(url, params)
    if response.status_code == 200:
        comments = {}
        for num, comment in enumerate(response.json()['data'], start=1):
            body = comment['body']
            time_posted = datetime.datetime.fromtimestamp(comment['created_utc']).strftime('%Y-%m-%d %H:%M')
            comments[num] = body, time_posted
        with open(f'{str(params["subreddit"])}-comments.json', 'w') as file:
            json.dump(comments, file, indent=4)
    elif response.status_code == 404:
        print("No such page", str(params["subreddit"]))


if __name__ == '__main__':
    with ProcessPoolExecutor(len(params)) as executor:
        executor.map(download_comments, params)
