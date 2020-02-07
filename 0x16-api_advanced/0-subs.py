#!/usr/bin/python3

"""
Module API for return number of subcriptons of reddit
"""
import requests


def number_of_subscribers(subreddit):
    """Function for return the number of number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent":  "arq-gabo"}
    r = requests.get(url, headers=headers)
    try:
        subs = r.json().get("data").get("subscribers")
        subscribers = subs if subs is not None else 0
        return(subscribers)
    except AttributeError:
        return(0)
