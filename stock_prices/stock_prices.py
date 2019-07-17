#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # for each pair of elems in list, substract the 1st from the 2nd
  # add that amount to results list
  # find the max number in that list -> the highest profit
  
  results = [] 

  for i in range(0, len(prices) - 1):
    for j in range(i+1, len(prices)):
      profit = prices[j] - prices[i]
      results.append(profit)

  profit = max(results)

  return profit





# Does it Match??
price_list1 = [1050, 270, 1540, 3800, 2] # 3530
price_list2 = [10, 7, 5, 8, 11, 9] # 6
price_list3 = [100, 90, 80, 50, 20, 10] # -10
price_list4 = [100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79] # 94

print("3530? ", find_max_profit(price_list1))
print("6? ",find_max_profit(price_list2))
print("-10? ",find_max_profit(price_list3))
print("94? ",find_max_profit(price_list4))





if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
