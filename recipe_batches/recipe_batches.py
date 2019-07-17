#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  set_tracker = {} # keeps track of no. complete sets of items we have

  for key_r in recipe:
    for key_i in ingredients:
      if key_r == key_i:

        # num of sets of that recipe ingredient we have available - round to lowest int
        value = ingredients[key_i] // recipe[key_r]

        # add item: value to tracker dictionary
        set_tracker[key_i] = value 

  # find minimum value in the dictionary and set that as batches
  # min(dictionary, key=dictionary.get) returns the KEY of the item in dictionary with the lowest value
  # so set that as the key in set_tracker[key] to return the minimum value in the dictionary
  batches = set_tracker[min(set_tracker, key=set_tracker.get)]

  print("Tracker Dictionary: ", set_tracker)
  print("Minimum Value: ", set_tracker[min(set_tracker, key=set_tracker.get)])

  return batches



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  # recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  # ingredients = { 'milk': 332, 'butter': 200, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients)) # using .format() instead of f-string


"""
### Notes:
- are the keys in same order in each dictionary?
- If not, iterate through each key in dict 1 arg (recipe) and iterate through each key in dict 2 arg (ingredients) to find matching
- If yes, comparing matching indices
- need empty batches = [] to keep track of how many recipies we can make
- If the value of matching key of dict 2 is >= that of value of the matching key of dict 1, then batches += 1

### Keeping track of how many complete sets of each recipe item are available:

- create dictionary to store # of complete sets for each food item
- complete_sets = {
  "item1" : 0,
  "item2" : 0,
  "item3" : 0
}
- num_complete_item = item in ingredients // item in recipe
- append new key value to complete_sets dictionary
  - key = name of that item
  - value = num_complete_item
- iterate over the values in complete_sets dictionary
- set batches = lowest value in complete_sets dictionary

- print batches

"""

"""
# First Commit:

def recipe_batches(recipe, ingredients):
  batches = 0
  num_items = len(recipe) 
  complete_items = 0

  for key_r in recipe:
    for key_i in ingredients:
      if key_r == key_i and ingredients[key_i] >= recipe[key_r]:
        complete_items += 1

    
    if complete_items == num_items:
      batches += 1

  print("Num Complete Items: ", complete_items)

  return batches

"""