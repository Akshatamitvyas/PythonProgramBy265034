# Write a Python program that outputs all possible strings formed by using
# the characters c , a , t , d , o , and g exactly once.

import random as rn
ch = ['c', 'a', 't', 'd', 'o', 'g']
rn.shuffle(ch)
print("-".join(ch))