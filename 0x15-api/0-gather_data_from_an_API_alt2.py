#!/usr/bin/python3
"""
HOW to Fetch Internet Resources Using The requests Package.
"""
import requests
import sys


def get_api_request(user):
    """
    Get info in JSON of the API url with requests Package.
    """
    url = 'https://jsonplaceholder.typicode.com/'

    # Get info user.
    path = 'users/'
    data = requests.get('{}{}{}'.format(url, path, user))
    d_info = data.json()
    print('Employee {} is done with tasks'.format(d_info['name']), end='')

    # Get info jobs for the user.
    path = 'todos?userId='
    data = requests.get('{}{}{}'.format(url, path, user))
    l_task = data.json()
    l_completed = list(filter(lambda item: item['completed' is True], l_task))
    print("({}/{}):".format(len(l_completed), len(l_task)))
    for task in l_completed:
        print("\t {}".format(task['title']))


if __name__ == '__main__':
    get_api_request(sys.argv[1])
