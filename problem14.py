#!/usr/bin/python
import numpy as np
from numpy import zeros
number_of_tests = 100
chainlengths = zeros(1000000000)

def next_in_sequence(x):
	output = 0
	if x != 1:
		if (x % 2) == 0:
			output = (x / 2)
		else:
			output = ((x * 3) + 1)
	return output

def chainlength(x):
	temp = x
	count = 0
	while temp != 1:
		if chainlengths[temp] == 0:
			temp = next_in_sequence(temp)
		else:
			chainlengths[x] = chainlengths[temp] + count
			break
		count += 1
	if chainlengths[x] == 0:
		chainlengths[x] = count

for i in range (2,number_of_tests):
	if chainlengths[i] == 0:
		chainlength(i)
#chainlength(2)
#chainlength(3)
print np.where(chainlengths==max(chainlengths))

