#!/usr/bin/python3

"""Module for export to in CSV file"""


import requests
import sys
import csv

if __name__ == '__main__':

    url = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1]))
    res = url.json()

    todo_list = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.
        format(sys.argv[1]))
    res2 = todo_list.json()

    with open('{}.csv'.format(sys.argv[1]), 'w') as r:
        r2 = csv.writer(r, quoting=csv.QUOTE_ALL)
        for i in res2:
            r2.writerow([i.get('userId'), res.get('username'),
                         i.get('completed'), i.get('title')])
