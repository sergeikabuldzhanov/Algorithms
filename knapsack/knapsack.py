#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])


def knapsack_solver(items, capacity):

    # base case for either no items or no capacity
    if capacity == 0 or len(items) == 0:
        return {'Value': 0, 'Chosen': []}
    item_in_question = items[-1]
    # if weight of the item in question is bigger than current capacity, look at the next item
    if item_in_question[1] > capacity:
        return knapsack_solver(items[:-1], capacity)
    else:
      # else consider taking and not taking the item in question
        not_take_item = knapsack_solver(items[:-1], capacity)
        take_item = knapsack_solver(
            items[:-1], capacity-item_in_question[1])
        take_item['Value'] += item_in_question[2]
        take_item['Chosen'] += [item_in_question[0]]
        return take_item if take_item['Value'] > not_take_item['Value'] else not_take_item


if __name__ == '__main__':
    if len(sys.argv) > 1:
        capacity = int(sys.argv[2])
        file_location = sys.argv[1].strip()
        file_contents = open(file_location, 'r')
        items = []

        for line in file_contents.readlines():
            data = line.rstrip().split()
            items.append(Item(int(data[0]), int(data[1]), int(data[2])))

        file_contents.close()
        print(knapsack_solver(items, capacity))
    else:
        print('Usage: knapsack.py [filename] [capacity]')
