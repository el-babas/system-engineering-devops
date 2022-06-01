#!/usr/bin/python3
"""
Recurse it!
Functions:
    matches_words
    recurse
    count_words
"""
import requests


def matches_words(list_posts, dict_words):
    """Function that counts the matches with the keywords.

    Args:
        list_posts (list): List of posts
        dict_words (dict): Dictionary of keywords.
    """
    for post in list_posts:
        for word in post.get('data').get('title').split():
            for key in dict_words.keys():
                if key.lower() == word.lower():
                    dict_words[key] += 1


def recurse(subreddit, dict_words, after=None):
    """Recursive function that queries the Reddit API and
    search keywords in titles posts.

    Args:
        subreddit (str): Reddit subscriber.
        dict_words (dict): Dictionary of words to look up.
        after (str, optional): After page.
    """
    api_header = {'User-Agent': 'Mozilla/5.0'}
    api_params = {'after': after}
    api_url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    api_res = requests.get(
                            api_url,
                            headers=api_header,
                            params=api_params,
                            allow_redirects=False
                          )
    if api_res.status_code != 200:
        return(None)

    # Data of father.
    api_data = api_res.json().get('data')
    # List children.
    list_posts = api_data.get('children')
    # Next Page
    after = api_data.get('after')

    matches_words(list_posts, dict_words)

    if after is None:
        return
    return recurse(subreddit, dict_words, after)


def count_words(subreddit, word_list):
    dict_words = dict()

    # Dictionary containing the words and repetitions
    for word in word_list:
        dict_words[word] = 0

    recurse(subreddit, dict_words)
    # ({k: v for k, v in sorted(dict_words.items(), key=lambda item: item[1])})
    list_sorted = sorted(dict_words.items(), key=lambda item: item[1]);
    list_sorted.reverse()
    for dupla in list_sorted:
        if dupla[1] != 0:
            print("{}: {}".format(dupla[0], dupla[1]))
