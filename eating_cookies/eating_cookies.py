#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution



def eating_cookies(n, cache=None):
  cache = { # initialize with base cases
    0: 1,
    1: 1,
    2: 2,
    3: 4
  }
  
  if n in cache:
    return cache[n]

  cache[n] = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3) # so cache[4] = 4 + 2 + 1 + 1 = 7

  return cache[n]

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')