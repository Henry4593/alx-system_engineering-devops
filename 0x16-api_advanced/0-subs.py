#!/usr/bin/python3
'''A module for interacting with the Reddit API.'''
import requests


BASE_URL = 'https://www.reddit.com'
'''The base URL for Reddit API requests.'''


def number_of_subscribers(subreddit):
    '''
    Fetch the subscriber count for a given subreddit.

    Args:
        subreddit (str): The subreddit to query.

    Returns:
        int: The number of subscribers, or 0 if the request fails.

    Note:This function sends a GET request to the Reddit API and parses the
    response.
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
    res = requests.get(
        '{}/r/{}/about/.json'.format(BASE_URL, subreddit),
        headers=api_headers,
        allow_redirects=False
    )
    if res.status_code == 200:
        return res.json()['data']['subscribers']
    return 0
