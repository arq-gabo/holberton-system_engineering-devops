#!/usr/bin/python3

"""Module for export to in CSV file"""

from requests import get
import requests
import sys
import json

if __name__ == '__main__':

    url = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1]))
    res = url.json()

    todo_list = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.
        format(sys.argv[1]))
    res2 = todo_list.json()

    with open('{}.json'.format(sys.argv[1]), 'w') as r:

        data = {}
        id_usr = res.get('id')
        data[id_usr] = []

        for i in res2:
            data[id_usr].append({
                "task": i.get("title"),
                "completed": i.get("completed"),
                "username": res.get("username")})

        json.dump(data, r)
