#!/usr/bin/python3
"""
100-main
"""
from sys import argv

if __name__ == '__main__':
    count_words = __import__('100-count').count_words
    if len(argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(argv[0]))
        print("Ex: {} programming 'python java javascript'".format(argv[0]))
    else:
        result = count_words(argv[1], [x for x in argv[2].split()])
