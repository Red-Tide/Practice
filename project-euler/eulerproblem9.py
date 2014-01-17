#!/usr/bin/python

'''Below you will see code that will solve kx(x+y)=500 a factored form of ka +
kb + kc = 1000 (with euclid's formula for generating pythagorean primitives
substituted in a,b,c) It then subsequently provides the solution for project euler
problem 9.'''

def triplet_test(k,x,y):
    if k*x*(x+y) == 500:
        return True
    else:
        return False


k = 1
x = 2
y = 1

while triplet_test(k,x,y) == False:
    if k*x*(x+y) > 500:
        if k == 1:
            y = y + 1
            x = y + 1
        else:
            k = 1
            x = x + 1
    else:
        k = k + 1

print((k*(x**2-y**2))*(k*(2*x*y))*(k*(x**2+y**2)))
