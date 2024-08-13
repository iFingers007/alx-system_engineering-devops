#!/usr/bin/python3
"""Module for RedditApi for Python"""
import requests


def top_ten(subreddit):
    """To get the number of subscribers"""

    url = f'https://www.reddit.com/dev/api/https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'subreddit-subscriber-checker/0.1'}
    params = {'limit': 10}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                print(post['data']['title'])
        else:
            print(None)
    except requests.RequestException:
        print(None)
