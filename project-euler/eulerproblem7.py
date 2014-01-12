#!/usr/bin/python

''' The below code tests for primacy, and solves problems 7 on project euler.It does so by taking a
    number a dividing it by all primes up until its square root. If any of the
    former primes divide equally into the the number it is not prime and is
    rejected as false; however if it will not be divided by previous primes it
    is prime and is added to the list of primes to divide into future numbers.
    The methodology is called the sieve of Eratosthenes:
    http://www.wikipedia.com/sieve_of_eratosthenes'''

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
