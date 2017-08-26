from math import sqrt
from numpy import zeros
from matplotlib import pyplot as plt
import time

def factors(n):
    # get factors and their counts
    factors = {}
    nn = n
    i = 2
    while i*i <= nn:
        while nn % i == 0:
            if not i in factors:
                factors[i] = 0
            factors[i] += 1
            nn //= i
        i += 1
    if nn > 1:
        factors[nn] = 1

    primes = list(factors.keys())

    # generates factors from primes[k:] subset
    def generate(k):
        if k == len(primes):
            yield 1
        else:
            rest = generate(k+1)
            prime = primes[k]
            for factor in rest:
                prime_to_i = 1
                # prime_to_i iterates prime**i values, i being all possible exponents
                for _ in range(factors[prime] + 1):
                    yield factor * prime_to_i
                    prime_to_i *= prime

    # in python3, `yield from generate(0)` would also work
    for factor in generate(0):
        yield factor

def find_amicables_under(limit):
	amicables = []
	for i in range(2,limit + 1):
		other_num = sum(factors(i)) - i
		if i != other_num:
			if sum(factors(other_num)) - other_num == i:
				amicables.append(i)
				amicables.append(other_num)
	return amicables

testnum = input("Find amicables up to what number? ")

xes = range(0,testnum)
yes = zeros(testnum)
for i in range(0,testnum,1000):
	then = time.time()
	result = set(find_amicables_under(i))
	now = time.time()
	yes[i] = now-then
	print result
	print "sum is : " + str(sum(result))

plt.scatter(xes,yes, color="k", s=12, marker="o")
plt.xlabel("Number")
plt.ylabel("Time")
plt.xlim(0,len(xes))
plt.ylim(0,max(yes)+1)
plt.title("Computation time vs. upper limit")
plt.show()
