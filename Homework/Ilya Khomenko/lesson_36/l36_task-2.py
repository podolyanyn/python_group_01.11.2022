import requests
import datetime
import json
# , 'sort': 'asc'
url = "https://api.pushshift.io/reddit/comment/search/"
params = {'subreddit': 'Ukrainian War', 'sort-type': 'created_utc'}
response = requests.get(url, params).json()

comments = {}
for num, comment in enumerate(response['data'], start=0):
    body = comment['body']
    time_posted = datetime.datetime.fromtimestamp(comment['created_utc']).strftime('%d-%m-%Y %H:%M')
    comments[num] = body, time_posted

    print(body)
    print(time_posted)



with open('test.json', 'w') as file:
    json.dump(comments, file, indent=4)