"""
Load data
Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/.
As a result, store all comments in chronological order in JSON and dump it to a file.
"""
import requests
import json

# Pushshift Reddit API Documentation
# https://github.com/pushshift/api


def download_subreddit_comments(question, subreddit, size):

    # URL for the Pushshift API endpoint
    api_url = f'https://api.pushshift.io/reddit/comment/search/?q={question}&subreddit={subreddit}&size={size}'
    resp = requests.get(api_url)

    if resp.status_code == 200:
        raw_comments = resp.json()['data']  # returns list of comments (stored as dict)

        comments = []

        # loop for retrieving only desired content
        for raw_comment in raw_comments:
            comment = {
                'author': raw_comment['author'],
                'body': raw_comment['body'],
                'utc_datetime_str': raw_comment['utc_datetime_str'],
                'link': f'https://www.reddit.com{raw_comment["permalink"]}'
            }
            comments.append(comment)

        # sort by date via API does not work (no idea why) -> so just reversed the list of comments
        comments = comments[::-1]

        with open(f'r_{subreddit}_comments.json', 'w') as f:
            json.dump(comments, f, indent=4)


if __name__ == '__main__':
    download_subreddit_comments('python', 'memes', 15)
