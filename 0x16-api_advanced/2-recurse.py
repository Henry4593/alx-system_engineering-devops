#!/usr/bin/python3
'''A module for interacting with the Reddit API.'''

import requests


BASE_URL = 'https://www.reddit.com'
'''Base URL for Reddit API requests.'''


def recurse(subreddit, hot_list=[], n=0, after=None):
    '''Retrieves a list of hot posts from a subreddit, recursively fetching
    more posts until all are retrieved.

    Args:
        subreddit (str): The subreddit to query. hot_list (list, optional):
        The list of hot posts to append to. Defaults to an empty list. n (int,
        optional): The count of posts to fetch. Defaults to 0.after (str,
        optional): The after parameter for pagination. Defaults to None.

    Returns:
        list: A list of hot post titles, or None if the request fails.
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
    sort = 'hot'
    limit = 30
    res = requests.get(
        '{}/r/{}/.json?sort={}&limit={}&count={}&after={}'.format(
            BASE_URL,
            subreddit,
            sort,
            limit,
            n,
            after if after else ''
        ),
        headers=api_headers,
        allow_redirects=False
    )
    if res.status_code == 200:
        data = res.json()['data']
        posts = data['children']
        count = len(posts)
        hot_list.extend(list(map(lambda x: x['data']['title'], posts)))
        if count >= limit and data['after']:
            return recurse(subreddit, hot_list, n + count, data['after'])
        else:
            return hot_list if hot_list else None
    else:
        return hot_list if hot_list else None
