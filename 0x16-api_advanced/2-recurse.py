#!/usr/bin/python3

"""
Module API return a list the titles in recursive form
"""
import requests


def recurse(subreddit, hot_list=[]):
    """Function recursive"""
    if len(hot_list) == 0:
        url = "https://api.reddit.com/r/{}/hot".format(subreddit)
        headers={"User-Agent": "arq-gabo"}
        requ = requests.get(url, headers=headers)
    else:
        idx = len(hot_list) - 1
        requ = requests.get(
            "https://api.reddit.com/r/{}/hot".format(subreddit),
            headers={"User-Agent": "cualquiera"},
            params={'after': hot_list[idx]})
        del hot_list[idx]
    if requ.status_code != 200:
        return(None)
    request = requ.json().get('data').get('children')
    for element in request:
        hot_list.append(element.get('data').get('title'))
    sig = requ.json().get('data').get('after')
    if sig is not None:
        hot_list.append(sig)
        return recurse(subreddit, hot_list)
    else:
        return(hot_list)
