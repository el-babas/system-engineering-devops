#!/usr/bin/python3
"""
    HOWTO Fetch Internet Resources Using The urllib Package.
"""
import json
import sys
import urllib.request


def get_api_request(user):
    url = 'https://jsonplaceholder.typicode.com/'

    # Get info user.
    path = 'users/'
    with urllib.request.urlopen('{}{}{}'.format(url, path, user)) as response:
        data = response.read().decode()
        try:
            d_info = json.loads(data)
        except BaseException:
            d_info = None
    print('Employee {} is done with tasks'.format(d_info['name']), end='')

    # Get info jobs for the user.
    path = 'todos?userId='
    with urllib.request.urlopen('{}{}{}'.format(url, path, user)) as response:
        data = response.read().decode()
        try:
            l_task = json.loads(data)
        except BaseException:
            l_task = None
    l_completed = list(filter(lambda item: item['completed'], l_task))
    print("({}/{}):".format(len(l_completed), len(l_task)))
    for task in l_completed:
        print("\t {}".format(task['title']))


if __name__ == '__main__':
    get_api_request(sys.argv[1])
