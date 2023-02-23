"""
Task 2. Requests using asyncio and aiohttp
Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ .
As a result, store all comments in chronological order in JSON and dump it to a file.
For this task use asyncio and aiohttp libraries for making requests to Reddit API.
"""
import json
import asyncio
import aiohttp
import datetime

# Pushshift Reddit API Documentation
# https://github.com/pushshift/api

requests_num = 24
comments_per_request = 499
all_comments = []
params = ('python', 'funny')


async def download_subreddit_comments(session, days_after, days_before):
    # URL for the Pushshift API endpoint
    api_url = f'https://api.pushshift.io/reddit/comment/search/?q={params[0]}&subreddit={params[1]}&size=' \
              f'{comments_per_request}&after={days_after}d&before={days_before}d'

    async with session.get(api_url) as resp:
        comments = []
        if resp.status == 200:
            raw_comments = await resp.json()  # returns a 'coroutine' object

            # loop for retrieving only desired content
            for raw_comment in raw_comments['data']:
                ts = int(raw_comment['created_utc'])
                dt = datetime.datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
                comment = {
                    'author': raw_comment['author'],
                    'body': raw_comment['body'],
                    'created_utc': raw_comment['created_utc'],
                    'date': dt,
                    'link': f'https://www.reddit.com{raw_comment["permalink"]}'
                }
                comments.append(comment)

        return comments


async def async_download():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(requests_num):
            days_after = (_ + 1) * 30
            days_before = _ * 30
            task = asyncio.create_task(download_subreddit_comments(session, days_after, days_before))
            tasks.append(task)

        # 'gather()' waits for all the tasks to complete
        results = await asyncio.gather(*tasks)

        for comments in results:
            all_comments.extend(comments)


if __name__ == '__main__':
    asyncio.run(async_download())

    # Sort the comments by timestamp
    all_comments.sort(key=lambda comment: comment['created_utc'])

    with open(f'r_{params[1]}_comments.json', 'w') as f:
        json.dump(all_comments, f, indent=4)
