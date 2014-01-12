#!/usr/bin/python

from numpy import *

generators = array([2,1])

def nextPyPrimitive(generators):
    a = generators[0]**2 - generators[1]**2
    b = 2 * generators[0] * generators[1]
    c =  generators[0]**2 + generators[1]**2
    return array([a,b,c])

y = 0

while y < 1000: 
    x = nextPyPrimitive(generators)
    y = sum(x)
    print(x)
    print(sum(x))
    generators[1] = generators[1]+1
