#!/usr/bin/python3

"""
Module API for return 10 active publications listed
"""
import requests


def top_ten(subreddit):
    """Function for return 10 active publications listed"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent":  "arq-gabo"}
    r = requests.get(url, headers=headers)
    post = r.json().get("data").get("children")
    try:
        act_sub = post[0].get('data').get('subreddit').lower()
        if len(post) > 0 and act_sub == subreddit.lower():
            for count, posts in enumerate(post):
                if count < 10:
                    print(posts.get("data").get("title"))
                else:
                    break
        else:
            print("None")
    except:
        print("None")
