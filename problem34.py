from math import factorial
def findfactorials():
	#for each number, get the digits from integers to strings to individual digits in an array
	factorialsum = 0
	for i in range(10,1000000):
		digits = [int(d) for d in str(i)]
		digitsum = 0
		for x in digits:
			digitsum += factorial(int(x))
		#print "The sum of the factorials of the digits of " + str(i) + " is " + str(digitsum)
		if digitsum == int(i):
			factorialsum += i
			print digits
	return factorialsum

print "The sum of all numbers that equal the sum of the factorial of their digits is " + str(findfactorials())