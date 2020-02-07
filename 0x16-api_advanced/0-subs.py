#!/usr/bin/python3

"""
Module REST API for return number of subcriptons of reddit
"""
import requests


def number_of_subscribers(subreddit):
    """Function for return the number of number of subscribers"""
    headers = {'User_Agent': 'arq-gabo'}
    try:
        reddit = get('https://www.reddit.com/r/{}/about.json'.format(
            subreddit), headers=headers).json()
        sub = reddit.get('data').get('subscribers')
        return(sub)
    except:
        return(0)
