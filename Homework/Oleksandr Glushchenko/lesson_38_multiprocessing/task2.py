"""
Task 2. Requests using concurrent and multiprocessing libraries
Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ .
As a result, store all comments in chronological order in JSON and dump it to a file.
For this task use concurrent and multiprocessing libraries for making requests to Reddit API.
"""
import requests
import json
from concurrent.futures import ThreadPoolExecutor, as_completed


# Pushshift Reddit API Documentation
# https://github.com/pushshift/api

threads_num = 8
requests_num = 500
comments_per_request = 100
all_comments = []
params = ('python', 'funny')


def download_subreddit_comments(days_after, days_before):
    # URL for the Pushshift API endpoint
    api_url = f'https://api.pushshift.io/reddit/comment/search/?q={params[0]}&subreddit={params[1]}&size=' \
              f'{comments_per_request}&after={days_after}d&before={days_before}d'
    resp = requests.get(api_url)
    comments = []
    if resp.status_code == 200:
        raw_comments = resp.json()['data']  # returns list of comments (stored as dict)

        # loop for retrieving only desired content
        for raw_comment in raw_comments:
            comment = {
                'author': raw_comment['author'],
                'body': raw_comment['body'],
                'created_utc': raw_comment['created_utc'],
                'link': f'https://www.reddit.com{raw_comment["permalink"]}'
            }
            comments.append(comment)

    return comments


def concurrent_download():
    with ThreadPoolExecutor(max_workers=threads_num) as executor:
        future_to_days = {}  # dict that maps futures with its params (days_after & days_before)
        for t in range(threads_num):
            days_after = (t + 1) * 30
            days_before = t * 30
            future = executor.submit(download_subreddit_comments, days_after, days_before)
            future_to_days[future] = (days_after, days_before)

        # 'as_completed()' waits for the futures to complete and returns an iterator over the completed futures
        for future in as_completed(future_to_days):  # iterating over the completed futures
            comments = future.result()
            all_comments.extend(comments)


if __name__ == '__main__':
    concurrent_download()

    # Sort the comments by timestamp
    all_comments.sort(key=lambda comment: comment['created_utc'])

    with open(f'r_{params[1]}_comments.json', 'w') as f:
        json.dump(all_comments, f, indent=4)
