#!/usr/bin/python3
"""
Checks student output for returning info from REST API
"""

import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"


def first_line(id):
    """ Fetch user name """

    resp = requests.get(users_url).json()

    name = None
    for i in resp:
        if i['id'] == id:
            name = i['name']

    filename = 'student_output'

    with open(filename, 'r') as f:
        first = f.readline().strip()

    if name in first:
        print("Employee Name: OK")
    else:
        print("Employee Name: Incorrect")


if __name__ == "__main__":
    first_line(int(sys.argv[1]))
