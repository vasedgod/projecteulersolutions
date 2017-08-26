#!/usr/bin/python

def squaresum(x):
	return (x * (x+1)/2) ** 2

def sumsquare(x):
	sum = 0
	for i in range(1,x+1):
		sum += i ** 2
	return sum

print "the difference is ", squaresum(100)-sumsquare(100)