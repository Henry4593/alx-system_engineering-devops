#!/usr/bin/python3
'''A module for interacting with the Reddit API.'''
import requests


BASE_URL = 'https://www.reddit.com'
'''Base URL for Reddit API requests.'''


def top_ten(subreddit):
    '''
        Fetch and print the titles of the top 10 posts from a subreddit.

    Args:
        subreddit (str): The subreddit to query.

    Returns:
        None

    Prints:
        The titles of the top 10 posts, or None if the request fails.
    '''
    api_headers = {
        'Accept': 'application/json',
        'User-Agent': ' '.join([
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'AppleWebKit/537.36 (KHTML, like Gecko)',
            'Chrome/97.0.4692.71',
            'Safari/537.36',
            'Edg/97.0.1072.62'
        ])
    }
    sort = 'top'
    limit = 10
    res = requests.get(
        '{}/r/{}/.json?sort={}&limit={}'.format(
            BASE_URL,
            subreddit,
            sort,
            limit
        ),
        headers=api_headers,
        allow_redirects=False
    )
    if res.status_code == 200:
        for post in res.json()['data']['children'][0:10]:
            print(post['data']['title'])
    else:
        print(None)
