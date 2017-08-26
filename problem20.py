#!/usr/bin/python
from scipy.special import factorial

def sumdigs(n):
	digis = list(str(n))
	sum = 0
	for i in xrange(0,len(digis)):
		sum += int(digis[0])
	return sum

print str(sumdigs(format(factorial(100),'.0f')))

#print "sum is " + str(sum(list(num)))
#evensum = 0
#for x in range(1,50):
#	if f(x) <= 4000000 and f(x) % 2 == 0:
#		evensum += f(x)

#print "sum of even-valued terms : ",evensum