#!/usr/bin/python3
'''A module for interacting with the Reddit API.'''

import requests


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
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
