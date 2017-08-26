#!/usr/bin/python

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

#currnum = 600851475143
#while is_prime(currnum) != True:#
#	currnum = currnum / next_factor(currnum)

print max(prime_factors(600851475143))