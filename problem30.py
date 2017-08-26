def getfifthpowersupto(n):
	output = []
	for i in range(10,n+1):
		numstring = str(i)
		numsum = 0
		for x in range(0,len(numstring)):
			numsum += int(numstring[x]) ** 5
		if i == numsum:
			output.append(i)
			print str(i) + " works!"
	return output

upperlimit = input("Test fifth powers up to: ")
print str(sum(getfifthpowersupto(upperlimit))) + " is the sum of all fifth power numbers."