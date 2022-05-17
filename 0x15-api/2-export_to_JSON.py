#!/usr/bin/python3
"""
HOW to Fetch Internet Resources Using The urllib Package.
"""
import json
import sys
import urllib.request


def get_api_request(user):
    """
    Get info in JSON of the API url with urllib Package.
    """
    url = 'https://jsonplaceholder.typicode.com/'

    # Get info user.
    path = 'users/'
    with urllib.request.urlopen('{}{}{}'.format(url, path, user)) as response:
        data = response.read().decode()
        try:
            d_info = json.loads(data)
        except BaseException:
            d_info = None

    # Get info jobs for the user.
    path = 'todos?userId='
    with urllib.request.urlopen('{}{}{}'.format(url, path, user)) as response:
        data = response.read().decode()
        try:
            l_task = json.loads(data)
        except BaseException:
            l_task = None

    l_json = []
    for task in l_task:
        l_json.append({
                        "task": task['title'],
                        "completed": task['completed'],
                        "username": d_info['username'],
                    })

    d_task = {str(user): l_json}
    filename = '{}.json'.format(user)
    with open(filename, mode='w') as json_file:
        json.dump(d_task, json_file)


if __name__ == '__main__':
    get_api_request(sys.argv[1])
