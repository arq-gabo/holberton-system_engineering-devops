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
    posts = r.json().get("data").get("children")
    try:
        actual_subreddit = posts[0].get('data').get('subreddit').lower()
        if len(posts) > 0 and actual_subreddit == subreddit.lower():
            for counter, post in enumerate(posts):
                if counter < 10:
                    print(post.get("data").get("title"))
                else:
                    break
        else:
            print("None")
    except:
        print("None")
