#!/usr/bin/python3
"""Queries the Reddit API and prints the titles of
the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API for the titles of the top 10 hot posts
    in a subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        try:
            data = response.json()
            posts = data["data"]["children"]
            for post in posts[:10]:
                print(post["data"]["title"])
        except KeyError:
            print(None)
    else:
        print(None)
