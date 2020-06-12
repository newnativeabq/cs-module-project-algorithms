#!/usr/bin/python

import sys
from collections import namedtuple
import numpy as np

Item = namedtuple('Item', ['index', 'size', 'value'])

# Global store
class G():
  pass

g = G()

# Path object & methods
class Path():
  def __init__(self, items=None):
    self.items = items

  def __str__(self):
    return f'<Path Object> len:{len(self.items)} size:{self.size} score:{self.score}'
  
  def add(self, item):
    if self.items is None:
      self.items = [item]
    else:
      self.items.append(item)

  def check(self, next_item, capacity):
    if self.size + next_item.size >= capacity:
      return False
    else:
      return True

  @property
  def score(self):
    temp = 0
    if self.items is not None:
      for item in self.items:
        temp += item.value
      return temp
    else:
      return 0

  @property
  def size(self):
    temp = 0
    if self.items is not None:
      for item in self.items:
        temp += item.size
      return temp
    else:
      return 0


class Cache():
  def __init__(self):
    self.cached_paths = {}

  @property
  def size(self):
    return len(self.cached_paths.keys())
  
  def cache_path(self, path, subset):
    new_key = self.generate_key(subset)
    if new_key in self.cached_paths:
      return False
    else:
      self.cached_paths[new_key] = path.score
      return True

  def generate_key(self, subset):
    if len(subset) >= 1:
      str_subset = '-'.join([str(x) for x in sorted(subset)])
    else:
      str_subset = ''
    return str_subset

  def search(self, directions, max_items=50):
    search_max = min(len(directions), max_items)
    for i in range(1, search_max):
      if self.generate_key(directions[0:i]) in self.cached_paths.keys():
        return True
    return False

  def sort_best(self):
    temp_list = []
    for key in self.cached_paths.keys():
      temp_list.append((key, self.cached_paths[key]))
    return sorted(temp_list, key = lambda x: x[1])[-1]



def get_cache():
  if hasattr(g, 'cache'):
    return g.cache
  else:
    g.cache = Cache()
    return g.cache


def cache_path(path=None, subset=None):
  active_cache = get_cache()
  return active_cache.cache_path(path=path, subset=subset)


##  Ok.  Now for an algorithm that does something useful
def search_stack(items, capacity):
  # explore a path and add the results to the cache
  def walk(items, directions, capacity):
    path = Path()
    steps = []
    for index in directions:
      if path.check(next_item=items[index], capacity=capacity):
        path.add(items[index])
        steps.append(index)
      else:
        cache_path(path=path, subset=steps)
        return

  i = 0
  cache = get_cache()
  while i < 10 * len(items):  # Control number of searches here
    directions = list(np.random.choice(list(range(len(items))), size=len(items),replace=False))
    if not cache.search(directions):
      walk(items, directions, capacity)
    i += 1
  return cache.sort_best()

### Making this better ###
#   Right now, it isnt' giving enough options a good shot.  Too random.
#   Add a locking mechanism that maintains a required start direction

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
    print(search_stack(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')