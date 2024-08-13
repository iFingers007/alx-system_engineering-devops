#!/usr/bin/python3
"""Module for RedditApi for Python"""
import requests


def number_of_subscribers(subreddit):
    """
    To get the number of subscribers

    Args:
    subreddit (str): Name of reddit to query

    """

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'kubuntu:konsole:v23.08.1 (by /u/0x83N3)'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        try:
            data = response.json()
            return data['data']['subscribers']
        except KeyError:
            return 0
    else:
        return 0
