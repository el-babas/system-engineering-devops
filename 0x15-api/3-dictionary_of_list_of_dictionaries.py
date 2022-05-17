#!/usr/bin/python3
"""
HOW to Fetch Internet Resources Using The urllib Package.
"""
import json
import requests
import urllib.request


def get_api_request():
    """
    Get info in JSON of the API url with urllib Package.
    """
    url = 'https://jsonplaceholder.typicode.com/'

    # Get info all users.
    path = 'users'
    with urllib.request.urlopen('{}{}'.format(url, path)) as response:
        data = response.read().decode()
        try:
            l_users = json.loads(data)
        except BaseException:
            l_users = None

    # Get info jobs for the user.
    filename = 'todo_all_employees.json'
    d_json = {}
    path = 'todos?userId='

    for user in l_users:
        username = user['username']
        userid = user['id']
        response = requests.get('{}{}{}'.format(url, path, userid))
        l_tasks = response.json()
        l_format = []
        for task in l_tasks:
            l_format.append({
                        "username": username,
                        "task": task['title'],
                        "completed": task['completed']
                        })
        d_json[str(userid)] = l_format

    with open(filename, mode='w') as f:
        json.dump(d_json, f)


if __name__ == '__main__':
    get_api_request()
