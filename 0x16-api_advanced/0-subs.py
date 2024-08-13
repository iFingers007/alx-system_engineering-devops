#!/usr/bin/python3
"""Module for RedditApi for Python"""
import requests


def number_of_subscribers(subreddit):
    """To get the number of subscribers"""

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'subreddit-subscriber-checker/0.1'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        try:
            data = response.json()
            return data['data']['subscribers']
        except KeyError:
            return 0
    else:
        return 0
