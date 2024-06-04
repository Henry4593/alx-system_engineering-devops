#!/usr/bin/python3
'''A module for interacting with the Reddit API.'''

import requests
from sys import argv


def top_ten(subreddit):
    '''
        Fetch and print the titles of the top 10 posts from a subreddit.

    Args:
        subreddit (str): The subreddit to query.

    Returns:
        The titles of the top 10 posts, or None if the request fails.
    '''
    user = {'User-Agent': 'Lizzie'}
    url = requests.get('https://www.reddit.com/r/{}/hot/.json?limit=10'
                       .format(subreddit), headers=user).json()
    try:
        for post in url.get('data').get('children'):
            print(post.get('data').get('title'))
    except Exception:
        print(None)


if __name__ == "__main__":
    top_ten(argv[1])
