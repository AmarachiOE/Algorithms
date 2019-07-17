#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches = 0
  num_items = len(recipe) # how many items are needed for recipe?
  # print("Num of Items: ", num_items)
  complete_items = 0

  for key_r in recipe:
    # print("Ingredients: ", item)
    for key_i in ingredients:
      if key_r == key_i and ingredients[key_i] >= recipe[key_r]:
        complete_items += 1

    if complete_items == num_items:
      batches += 1

  return batches



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients)) # using .format() instead of f-string


"""
Notes:
- are the keys in same order in each dictionary?
- If not, iterate through each key in dict 1 arg (recipe) and iterate through each key in dict 2 arg (ingredients) to find matching
- If yes, comparing matching indices
- need empty batches = [] to keep track of how many recipies we can make
- If the value of matching key of dict 2 is >= that of value of the matching key of dict 1, then batches += 1

"""