#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
cache = {}
def eating_cookies(n, count=0):
  if n == 0:
    return 1
  elif n < 0:
    return 0
  elif n in cache.keys():
    return cache[n]
  elif n >= 1:
    count += eating_cookies(n=n-1, count=count)\
            + eating_cookies(n=n-2, count=count)\
            + eating_cookies(n=n-3, count=count)
    # print('n:{}, count:{}'.format(n, count))
    cache[n] = count
    # print(cache)
  return count

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')