# Load data
# Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ .
# As a result, store all comments in chronological order in JSON and dump it to a file.

import requests


def subreddit_comments_to_txt(subreddit):

    def subreddit_comments(subreddit):
        url = 'https://api.pushshift.io/reddit/comment/search/'
        request = requests.get(url, params={'subreddit': subreddit})
        return request.json()

    count = 1
    for comment in subreddit_comments(subreddit)['data']:
        sep = ' '+'#'*50+' '
        data = f'{sep}{count}{sep}\n{comment["body"]}\n\n'
        with open(f'{subreddit}.txt', 'a') as file:
            file.write(data)
        count += 1


if __name__ == '__main__':
    i = 1
    lis = []
    while True:
        looking_for = input(f'{i}. I am looking for or <S> stop: ')
        if looking_for.lower() == 's':
            break
        lis.append(looking_for)
        i += 1

    for subreddit in lis:
        subreddit_comments_to_txt(subreddit)

