#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    per_ing_list = []
    for k, v in recipe.items(): # O of n
        if k in ingredients: # probably just an O(1)
            per_ing_list.append(ingredients[k]//v) # O(n)? depends of pythons implementation of lists
        else:
            return 0
    return min(per_ing_list) #Either O(n) or O(n^2)


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
