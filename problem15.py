#!/usr/bin/python
import random
import numpy as np
import itertools as it

# def numpathsofsquaresize(n):
# 	gridlist = np.empty([1,2*n])
# 	grid = np.zeros(2*n)
# 	for y in xrange(0,pow(n,3)):
# 		for x in xrange(0,n*2):
# 			grid[x] = random.choice([0,1])
# 		if sum(grid) == n:
# 			np.append(gridlist,grid)
# 			print gridlist
# 	uniquegrids = list(set(gridlist.flatten()))
# 	return len(uniquegrids)

def generatePrintBinary(n):
    # Create an empty queue
    from Queue import Queue
    q = Queue()

    # Enqueu the first binary number
    q.put("1")

    # This loop is like BFS of a tree with 1 as root
    # 0 as left child and 1 as right child and so on
    while(n>0):
        n-= 1
        # Print the front of queue
        s1 = q.get() 
        print s1 

        s2 = s1 # Store s1 before changing it

        # Append "0" to s1 and enqueue it
        q.put(s1+"0")

        # Append "1" to s2 and enqueue it. Note that s2
        # contains the previous front
        q.put(s2+"1")

print generatePrintBinary(4)
# squaresize = input('How many units wide is the square?')
# print numpathsofsquaresize(squaresize)



# for 2x2,
# 2 rights and 2 downs in any combo
# R R D D
# R D R D
# R D D R
# D R R D
# D R D R
# D D R R
# 6 ways

# for 3x3
# 3 rights and 3 lefts in any combo
# R R R D D D
# R R D R D D
# R D R R D D
# D R R R D D
# R R D D R D
# R D D R R D
# D D R R R D
# R R D D D R
# R D D D R R
# D D D R R R
# 10 ways