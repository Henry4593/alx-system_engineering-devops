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


def number_of_subscribers(subreddit):
    '''Fetch the subscriber count for a given subreddit.

    Args:
        subreddit (str): The subreddit to query.

    Returns:
        int: The number of subscribers, or 0 if the request fails.

    Note: This function sends a GET request to the Reddit API and parses the
    response.
    '''
    try:
        session = get_session()
        url = f"https://www.reddit.com/r/{subreddit}/about.json"
        response = session.get(url, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get("data")
            num_of_subscribers = data.get("subscribers")
            return num_of_subscribers
        return 0

    except requests.exceptions.RequestException:
        return 0
