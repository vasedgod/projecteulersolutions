""" Find the largest prime factor less than 600851475143"""
def prime_factors(testnum):
    """Find all factors of testnum and return as a list"""
    i = 2
    factors = []
    while i <= testnum ** 0.5:
    #no need to check higher than sqrt(n)
        if testnum % i:
            i += 1
        else:
            testnum //= i
            #if i factors evenly, divide it out and test
            #with the remaining number
            factors.append(i)
    if testnum > 1:
        factors.append(testnum)
    return factors

print "The maximum prime factor of 600851475143 is " + str(max(prime_factors(600851475143)))
