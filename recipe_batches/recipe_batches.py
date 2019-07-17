#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # will keep track of # complete sets of items
  set_tracker = {} 

  for key_r in recipe:
    for key_i in ingredients:
      if key_r == key_i:

        # num of sets of that recipe-ingredient we have available - round to lowest int with //
        value = ingredients[key_i] // recipe[key_r]

        # add item: value to tracker dictionary
        set_tracker[key_i] = value 

    # Handle when item in recipe isn't in ingredients
    # Add that key to tracker dictionary with value 0
    if ingredients.get(key_r) == None:
      set_tracker[key_r] = 0


  batches = min(set_tracker.values())


  # print("Tracker Dictionary: ", set_tracker)
  # print("Minimum Value: ", min(set_tracker.values()))
  # print("Batches: ", batches)
  return batches



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  # Original (batches = 0)
  # recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  # ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }

  # When Multiple Sets Available (batches > 1)
  # recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  # ingredients = { 'milk': 332, 'butter': 200, 'flour': 51 }

  # When Recipe has items not listed in Ingredients
  recipe = { 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }
  ingredients = { 'milk': 1288, 'flour': 9, 'sugar': 95 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients)) # using .format() instead of f-string


"""
### Notes:
- are the keys in same order in each dictionary?
- If not, iterate through each key in dict 1 arg (recipe) and iterate through each key in dict 2 arg (ingredients) to find matching
- If yes, comparing matching indices
- need empty batches = [] to keep track of how many recipies we can make
- If the value of matching key of dict 2 is >= that of value of the matching key of dict 1, then batches += 1

### NEW: Keeping track of how many complete sets of each recipe item are available:

- create dictionary to store # of complete sets for each food item
- set_tracker = {
  "item1" : 0,
  "item2" : 0,
  "item3" : 0
}
- value = item in ingredients // item in recipe
- append new key: value to set_tracker dictionary
  - key = name of that item
  - value = value
  - set_tracker[key_in_list]: value

- find minimum value in the dictionary and set that to batches variable
  - dictionary.values() returns list of all values in dictionary
  - set batches = lowest value in set_tracker dictionary

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