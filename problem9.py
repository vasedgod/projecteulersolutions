#!/usr/bin/python

tests = []
for i in range(1,998):
	for j in range(1,998):
		tests.append([i, j, 1000-j-i])

for combo in tests:
	if combo[0]**2 + combo[1]**2 == combo[2]**2:
		print "product of a*b*c = ", combo[0]*combo[1]*combo[2]