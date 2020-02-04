!#/usr/bin/python3

"""Module using REST API return information TODO list progress
given employed ID"""


import requests
import sys
import json


if __name__ == '__main__':

    request = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1]))
    res = request.json()
    print(res)
