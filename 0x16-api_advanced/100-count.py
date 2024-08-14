#!/usr/bin/python3
"""Queries the Reddit API,
parses the title of all hot articles
"""
import requests


def count_words(subreddit, word_list, hot_list=[], after=None):
    """
    queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords

    Args:
    subreddit (str): Subbredit args
    word_list (str): Word List
    hot_list (list): List of hot api
    after (str): Pagination marker for next page

    Returns:
    None
    """

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'word-count-bot/0.1'})
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)  # noqa
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            hot_list.extend(post['data']['title'].lower().split() for post in posts)  # noqa

            after = data['data'].get('after')
            if after:
                return count_words(subreddit, word_list, hot_list, after)
            else:
                return process_words(hot_list, word_list)
        else:
            return
    except requests.RequestException:
        return


def process_words(hot_list, word_list):
    """
    processes words
    Args:
    hot_list (list): hot list
    word_list (list): list of words
    """

    word_count = {}
    for title_words in hot_list:
        for word in title_words:
            # Normalize words and match only exact words (avoid substrings)
            word = word.strip('.,!?_-')  # Strip punctuations around the words
            if word in map(str.lower, word_list):
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

    # Sort by count (descending) then alphabetically by keyword (ascending)
    sorted_words = sorted(word_count.items(), key=lambda item: (-item[1], item[0]))  # noqa

    for word, count in sorted_words:
        print(f"{word}: {count}")
