#!/usr/bin/python

def primeTest(testNum,primes):
    for prime in primes:
        if prime > (testNum**0.5):
            return testNum
        else:
            if testNum%prime == 0:
                return False
            

primes = [2,3]
testNum = 4

while len(primes) < 10001:
    test = primeTest(testNum,primes)
    if test != False:
        primes.append(test)
    testNum = testNum +1
print(primes[-1], len(primes))
