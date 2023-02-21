"""
Task3. Requests using multiprocessing
Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ .
As a result, store all comments in chronological order in JSON and dump it to a file.
For this task use Threads for making requests to reddit API.
"""
import requests
import json
import threading


# Pushshift Reddit API Documentation
# https://github.com/pushshift/api

threads_num = 5
requests_num = 500
comments_per_request = 100
all_comments = []
lock = threading.Lock()
params = ('python', 'memes')


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

        # sort by date via API does not work (no idea why) -> so just reversed the list of comments
        comments = comments[::-1]
    return comments


def threaded_download(days_after, days_before):
    comments = download_subreddit_comments(days_after, days_before)
    with lock:
        all_comments.extend(comments)


threads = []
for t in range(threads_num):
    days_after = (t + 1) * 30
    days_before = t * 30
    thread = threading.Thread(target=threaded_download, args=(days_after, days_before))
    threads.append(thread)
    thread.start()

# Wait for all the threads to finish
for thread in threads:
    thread.join()

# Sort the comments by timestamp
all_comments.sort(key=lambda comment: comment['created_utc'])


with open(f'r_{params[1]}_comments.json', 'w') as f:
    json.dump(all_comments, f, indent=4)
