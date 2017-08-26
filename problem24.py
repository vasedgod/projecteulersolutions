import itertools

output = sorted(list(itertools.permutations([0,1,2,3,4,5,6,7,8,9],10)))
print "The millionth lexicographic permutation is " + str(output[999999])