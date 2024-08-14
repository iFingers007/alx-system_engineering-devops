#!/usr/bin/python3
import requests
"""Queries the Reddit API and prints the titles of
the first 10 hot posts listed for a given subreddit.
"""


def top_ten(subreddit):
    """
    Queries the Reddit API for the titles of the top 10 hot posts
    in a subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    """

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'subreddit-top-ten/0.1'}
    params = {'limit': 10}  # Limit to the first 10 posts

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)  # noqa

        # Check if the status code is 200 (OK)
        if response.status_code != 200:
            print(None)
            return

        try:
            data = response.json()
        except ValueError:
            # If the response cannot be parsed as JSON, print None and return
            print(None)
            return

        posts = data.get('data', {}).get('children', [])
        if not posts:
            print(None)
            return

        for post in posts:
            print(post['data']['title'])

    except requests.RequestException as e:
        print(None)
        return
