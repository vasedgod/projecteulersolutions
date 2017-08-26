#!/usr/bin/python

def is_prime(n):
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def xprime(x):
	primes = [2,3]
	testnum = 1
	while len(primes) <= x:
		if is_prime(6*testnum-1):
			primes.append(6*testnum-1)
		if is_prime(6*testnum+1):
			primes.append(6*testnum+1)
		testnum += 1
	return primes

print xprime(10001)[10000]
