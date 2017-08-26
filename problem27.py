from math import sqrt; from itertools import count, islice

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def primecount(a,b):
	primecount = 0
	i = 0
	currnum = i ** 2 + a * i + b
	while isPrime(currnum):
		primecount += 1
		i += 1
		currnum = i ** 2 + a * i + b
	return primecount

maxprimes = [0, 0, 0]
for i in range(-999,1000):
	for j in range(-1000,1000):
		if primecount(i,j) > maxprimes[0]:
			maxprimes[0] = primecount(i,j)
			maxprimes[1] = i
			maxprimes[2] = j

print "a = " + str(maxprimes[1]) + " and b = " + str(maxprimes[2]) + " have the most consecutive primes, with " + str(maxprimes[0]) + " primes."
print " and a product of " + str(maxprimes[1] * maxprimes[2])