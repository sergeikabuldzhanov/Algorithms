#!/usr/bin/python

import sys


def making_change(amount, denominations, cache={}):
    table = [0 for k in range(amount+1)]

    # Base case (If given amount is 0)
    table[0] = 1

    for i in range(0, len(denominations)): #for each denomination
        for j in range(denominations[i], amount+1): #for each j starting from that denomination to amount
            table[j] += table[j-denominations[i]] # number of solutions is equal to number of solutions for previous denominations + number of solutions for that amount - that denomination
    return table[amount] # return final count


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
