import multiprocessing

import requests
import datetime
import json
from multiprocessing import Pool

params = [{'subreddit': 'walking', 'sort-type': 'created_utc'},
          {'subreddit': 'chill', 'sort-type': 'created_utc'},
          {'subreddit': 'python web_scraping', 'sort-type': 'created_utc'}]

def comments(params):
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




if __name__ == '__main__':
    with Pool(10) as p:
        records = p.map(comments, params)

