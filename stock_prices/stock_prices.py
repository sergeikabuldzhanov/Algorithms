#!/usr/bin/python

import argparse

def find_max_profit(prices):
  profit = prices[1] - prices[0]
  for i in range(len(prices)): # big O of n
    for j in range(i+1, len(prices)): # O of n/2 on overage
      diff = prices[j]-prices[i]
      profit = diff if diff > profit else profit
  return profit # O of n^2 in the end


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))