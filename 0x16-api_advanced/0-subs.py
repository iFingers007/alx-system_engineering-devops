#!/usr/bin/python3
"""Module for RedditApi for Python"""
import requests


def number_of_subscribers(subreddit):
    """
    To get the number of subscribers

    Args:
    subreddit (str): Name of reddit to query

    """

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'subreddit-subscriber-checker/0.1'})
#    headers = {'User-Agent': 'subreddit-subscriber-checker/0.1'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data'].get('subscribers', 0)
        else:
            return 0
    except requests.RequestException:
        return 0

#    url = f"https://www.reddit.com/r/{subreddit}/about.json"
#    user_agent = requests.utils.default_headers()
#    user_agent.update({'User-Agent': 'My User Agent 1.0'})
#    response = requests.get(url, headers=user_agent)

#    if response.status_code == 200:
#        try:
#            data = response.json()
#            return data['data']['subscribers']
#        except KeyError:
#            return 0
#    else:
#        return 0

#    r = requests.get(url, headers=headers).json()
#    subscribers = r.get('data', {}).get('subscribers')
#    if not subscribers:
#        return 0
#    return subscribers

#    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
#    headers = {'User-Agent': 'subreddit-subscriber-checker/0.1'}
#
