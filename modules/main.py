import utility
print(utility) # if u run this we have the directory of the utlity and we generate __pycache__
# this __pycache__ will appear everytime we run a file with import a module
print(utility.multiply(5,8))
# another way of importing is like this
from shopping.more_shopping.shopping_cart import buy
print(buy('chicken'))

import shopping.more_shopping.shopping_cart
print(shopping.more_shopping.shopping_cart)

print(shopping.more_shopping.shopping_cart.buy('apple'))

from utility import multiply
print(utility.multiply(2,55))

from shopping import shopping_cart
print(shopping_cart.buy('zari'))