#!/usr/bin/python3

"""Module using REST API return information TODO list progress
given employed ID"""


import requests
import sys
import json


if __name__ == '__main__':

    url = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1]))
    res = url.json()

    todo_list = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(sys.argv[1]))
    res2 = todo_list.json()
    print(res2)


"""
    name_employe = res['name']
    print("Employee {} is done with:".format(name_employe)
"""
