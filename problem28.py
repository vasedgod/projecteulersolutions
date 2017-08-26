import matplotlib.pyplot as plt
import time
from numpy import zeros

def spiraldiagsum(sidelength):
	if sidelength % 2 == 0:
		return "Bad side length, must be even."
	diagsum = 0
	currnum = 0
	rowdiff = 2
	for i in range(1,sidelength+1,2):
		if i == 1:
			currnum = 1
			diagsum += currnum
		else:
			currnum += rowdiff
			diagsum += currnum
			currnum += rowdiff
			diagsum += currnum
			currnum += rowdiff
			diagsum += currnum
			currnum += rowdiff
			diagsum += currnum
			rowdiff+=2
	return diagsum

maxtest = 10000001
xes = range(0,maxtest+1)
yes = zeros(maxtest+1)
for i in xrange(1,maxtest,100002):
	then = time.time()
	spiraldiagsum(i)
	now = time.time()
	yes[i] = now-then
plt.scatter(xes,yes, color="k", s=12, marker="o")
plt.xlabel("Spiral size (width)")
plt.ylabel("Time to compute")
plt.xlim(0,len(xes))
plt.ylim(0,max(yes)*1.1)
plt.title("Calculating diagonal sums of spirals of side length x")
plt.show()

#testlength = input("How wide of a spiral? ")
#print str(spiraldiagsum(testlength))
