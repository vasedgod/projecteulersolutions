#!/usr/bin/python

def sum_digits(n):
	arr = list(str(n))
	for x in xrange(0,len(arr):
		arr[x] = int(arr[x])
	return sum(arr)

testnum = input("What number to count digits?")
print sum_digits(testnum)