#!/usr/bin/python3
"""Recursive function that queries the Reddit API
and returns a list containing the titles of all
hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively fetches all hot article titles from a
    subreddit using the Reddit API.
    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list, optional): List to store the titles. Defaults to [].
        after (str, optional): pagination marker for the next page.
        Defaults to None.

    Returns:
    list: List pf article titles, or None if an error occurs or the
    subreddit is invalid
    """

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)  # noqa
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            hot_list.extend(post['data']['title'] for post in posts)

            # Check if there's another page to load
            after = data['data'].get('after')
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except requests.RequestException:
        return None
