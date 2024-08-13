#!/usr/bin/python3
'''A module for interacting with the Reddit API.'''

import requests


def get_session():
    """Create a requests session with the appropriate headers."""
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\
        /537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    })
    return session


def top_ten(subreddit):
    '''Fetch and print the titles of the top 10 posts from a subreddit.

    Args:
        subreddit (str): The subreddit to query.

    Returns:
        The titles of the top 10 posts, or None if the request fails.
    '''
    session = get_session()
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json?limit=10'
    response = session.get(url, allow_redirects=False).json()
    try:
        for post in response.get('data').get('children'):
            print(post.get('data').get('title'))
    except Exception:
        print(None)
