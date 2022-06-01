#!/usr/bin/python3
"""
2-main
"""
from sys import argv

if __name__ == '__main__':
    recurse = __import__('2-recurse').recurse
    if len(argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
