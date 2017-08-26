from math import sqrt
from itertools import count, islice

def isprime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def getcircularprimes(max):
	circularprimes = []
	for i in range(1, max):
		istr = str(i)
		if isprime(i) and len(istr) == 1:
			circularprimes.append(i)
		if i == "11":
			circularprimes.append(11)
		teststr = istr[1:len(istr)]+istr[0]
		while teststr != istr:
			if isprime(int(teststr)) and isprime(int(teststr[::-1])):
				circularprimes.append(int(teststr))
				circularprimes.append(int(teststr[::-1]))
				teststr = teststr[1:len(teststr)]+teststr[0]
			else:
				teststr = istr
		if teststr == istr and isprime(teststr):
			circularprimes.append(teststr)
	return set(circularprimes)

#print "6 is a prime is : " + str(isprime(6))
testmax = input("Find circular primes up to?")
print str(len(getcircularprimes(testmax))) + " circular primes up to " + str(testmax) + " are " + str(sorted(getcircularprimes(testmax)))