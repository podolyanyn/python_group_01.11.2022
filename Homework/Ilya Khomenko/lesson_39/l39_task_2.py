import asyncio
import aiohttp
import time
import json
import datetime

url = 'https://api.pushshift.io/reddit/comment/search/'


parm = [{'subreddit': 'T-Siries', 'sort-type': 'created_utc'},
          {'subreddit': 'Blockchain', 'sort-type': 'created_utc'},
          {'subreddit': 'Watermelon', 'sort-type': 'created_utc'}]



async def download(url, params):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            response = await response.json()
            comments = {}
            for num, comment in enumerate(response['data'], start=1):
                body = comment['body']
                time_posted = datetime.datetime.fromtimestamp(comment['created_utc']).strftime('%Y-%m-%d %H:%M')
                comments[num] = body, time_posted
            with open(f'comments-{params["subreddit"]}.json', 'w') as file:
                json.dump(comments, file, indent=4)

async def main():
    tasks = []
    for par in parm:
        tasks.append(asyncio.create_task(download(url, par)))
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print(time.time() - start)