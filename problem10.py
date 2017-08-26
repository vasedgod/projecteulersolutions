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

def sumprime(x):
	testnum = 1
	sum = 5
	while 6*testnum+1 < x:
		if is_prime(6*testnum-1):
			sum+= 6*testnum-1
		if is_prime(6*testnum+1):
			sum+= 6*testnum+1
		testnum += 1
	return sum

print sumprime(2000000)