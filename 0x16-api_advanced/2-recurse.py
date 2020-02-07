#!/usr/bin/python3

"""
Module API return a list the titles in recursive form
"""
import requests


def recurse(subreddit, counter=0, after=None, hot_list=[]):
    """Function recursive"""
    if counter != 0 and after is None:
        return(hot_list)
    headers = {"User-Agent": "arq-gabo"}
    payload = {} if counter == 0 else {'after': after, 'count': 25}
    url = 'https://www.reddit.com/r/{}.json'.format(subreddit)
    r = requests.get(url, headers=headers, allow_redirects=False,
                     params=payload)
    ps = r.json().get("data").get("children")
    posts = [post.get("data").get("title") for post in ps]
    after = r.json().get("data").get("after")
    hot_list = hot_list + posts
    return recurse(subreddit, hot_list + posts, counter+1, after)
