import requests
import datetime
import json
from concurrent.futures import ProcessPoolExecutor as ProcPool


params = [{'subreddit': 'testing', 'sort-type': 'created_utc'},
          {'subreddit': 'workout', 'sort-type': 'created_utc'},
          {'subreddit': 'religion', 'sort-type': 'created_utc'}]

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
    with ProcPool(len(params)) as p:
        p.map(comments, params)

