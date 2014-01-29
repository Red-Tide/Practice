#!/usr/bin/python

'''A list comprehension creates a list from 1 to 1000, but only accepts
elements that are divisible by 3 or 5.'''

x = [x for x in range(1,1000) if x % 3 == 0 or x % 5 == 0]
print(sum(x))
