#!/usr/bin/python

testnum = 20

while testnum > 0:
	i = 1
	total = 0
	while i <= 20:
		if testnum % i == 0:
			total += 1
		i += 1
	if total == 20:
		print testnum
		break
	else:
		testnum += 20
