#!/usr/bin/python

import sys


def rock_paper_scissors(n, cache={}):
    words = ["rock", "paper", "scissors"]
    if n == 0:
        return [[]]
    if n in cache:
        return cache[n]
    elif n >= 1:
        next_list = []
        for lst in rock_paper_scissors(n-1):
            for word in words:
                next_list.append(lst+[word])
        cache[n] = next_list
        return next_list


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
