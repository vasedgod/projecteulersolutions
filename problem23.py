#!/usr/bin/python
from math import sqrt
import matplotlib.pyplot as plt
from numpy import zeros
from matplotlib.lines import Line2D

def factors(n): #Get all the factors in a set
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(sqrt(n)) + 1) if n % i == 0)))

def sumoffactors(input_num): #sum up the factors
	factorssum = 0
	factors_of_num = factors(input_num)
	if len(factors_of_num) == 2:
		return 0
	for x in factors_of_num:
		factorssum += x
	return factorssum-input_num

def find_abundant_numbers(n):
	xes = range(0,n+1)
	yes = zeros(n+1)
	abundants = []
	for i in xrange(12,n+1):
		if sumoffactors(i) > i:
			print "sum of factors of " + str(i) + " = " + str(sumoffactors(i))
			abundants.append(i)
			yes[i] = 1
	plt.scatter(xes,yes, color="k", s=12, marker="o")
	plt.xlabel("Number")
	plt.ylabel("Yes (1) or No (0)")
	plt.xlim(0,len(xes))
	plt.ylim(0,2)
	plt.title("Numbers whose factorsums total 1 more than the original")
	#print str(xes)
	#print str(yes)
	#plt.show()
	return abundants


#find abundant numbers
testnum = input("Compute abundant numbers up to : ")
abundants = find_abundant_numbers(testnum)
#print abundants

sumslist = []
for i in range(0,len(abundants)):
	for j in range(0,len(abundants)):
		sumslist.append(abundants[i]+abundants[j])
#print sumslist
print set(sumslist)
print "sum of 1 to " + testnum + " - sum(sumslist) = " + str(testnum*(testnum+1)/2-sum(set(sumslist)))

