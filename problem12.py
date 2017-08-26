#!/usr/bin/python
from math import sqrt
def num_factors(n):
    return len(set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(sqrt(n)) + 1) if n % i == 0))))

def findnum(factorcount):
	tricount = 2
	currnum = 1
	while num_factors(currnum) <= factorcount:
		currnum += tricount
		tricount += 1
		print str(currnum) + " has " + str(num_factors(currnum)) + " factors."
	return currnum

factors = input("How many factors are we looking to find?")
#print str(factors) + " has " + str(num_factors(factors)) + " factors."
print "The first number to have "+str(factors)+" factors is " + str(findnum(factors))	