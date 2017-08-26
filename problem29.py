def getterms(amax,bmax):
	allterms = []
	for a in range (2,amax+1):
		for b in range (2,bmax+1):
			allterms.append(a ** b)
	return set(allterms)

print len(getterms(100,100))