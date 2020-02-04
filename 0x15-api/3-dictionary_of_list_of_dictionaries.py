#!/usr/bin/python3

"""Export to json file all user"""

from requests import get
import json

if __name__ == '__main__':

    user_dic = get('https://jsonplaceholder.typicode.com/users/').json()

    todo_dic = get('https://jsonplaceholder.typicode.com/todos/').json()

    with open('todo_all_employees.json', 'w') as r:
        data = {}
        for i in user_dic:
            data[i.get('id')] = []
            for j in todo_dic:
                if i.get('id') == j.get('userId'):
                    data[i.get('id')].append({
                        "task": j.get("title"),
                        "completed": j.get("completed"),
                        "username": i.get("username")})
        json.dump(data, r)
