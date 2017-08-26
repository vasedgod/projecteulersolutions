#!/usr/bin/python

def next_in_sequence(x):
	output = 0
	if x != 1:
		if (x % 2) == 0:
			output = (x / 2)
		else:
			output = ((x * 3) + 1)
	return output

def collatz(n):
	