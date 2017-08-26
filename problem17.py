#!/usr/bin/python

def number_to_words(n):
	wordlist = []
	num = list(str(n))
	#if number is in the thousands
	if len(num) == 4:
		if num[0] == '1':
			wordlist.append("one")
		elif num[0] == '2':
			wordlist.append("two")
		elif num[0] == '3':
			wordlist.append("three")
		elif num[0] == '4':
			wordlist.append("four")
		elif num[0] == '5':
			wordlist.append("five")
		elif num[0] == '6':
			wordlist.append("six")
		elif num[0] == '7':
			wordlist.append("seven")
		elif num[0] == '8':
			wordlist.append("eight")
		elif num[0] == '9':
			wordlist.append("nine")
		wordlist.append("thousand")
		if num[1] == '0' and num[2] == '0' and num[3] == '0':
			return wordlist
		num = num[1:len(num)]
		#print "At step len=4 num = " + str(num)
	#if number is in hundreds
	if len(num) == 3 and num[0] != 0:
		if num[0] == '1':
			wordlist.append("one")
		elif num[0] == '2':
			wordlist.append("two")
		elif num[0] == '3':
			wordlist.append("three")
		elif num[0] == '4':
			wordlist.append("four")
		elif num[0] == '5':
			wordlist.append("five")
		elif num[0] == '6':
			wordlist.append("six")
		elif num[0] == '7':
			wordlist.append("seven")
		elif num[0] == '8':
			wordlist.append("eight")
		elif num[0] == '9':
			wordlist.append("nine")
		wordlist.append("hundred")
		#print num
		if (num[1] != '0' and num[2] != '0') or (num[1] == '0' and num[2] !='0') or (num[1] != '0' and num[2] == '0'):
			wordlist.append("and")
		num = num[1:len(num)+1]
		#print ")At step len=3 num = " + str(num)
	#if number is tens digit and change
	if len(num) == 2:
		if int(num[0]) > 1 or int(num[0]) == 0:
			if num[0] == '2':
				wordlist.append("twenty")
			elif num[0] == '3':
				wordlist.append("thirty")
			elif num[0] == '4':
				wordlist.append("forty")
			elif num[0] == '5':
				wordlist.append("fifty")
			elif num[0] == '6':
				wordlist.append("sixty")
			elif num[0] == '7':
				wordlist.append("seventy")
			elif num[0] == '8':
				wordlist.append("eighty")
			elif num[0] == '9':
				wordlist.append("ninety")
			if num[1] == '1':
				wordlist.append("one")
			elif num[1] == '2':
				wordlist.append("two")
			elif num[1] == '3':
				wordlist.append("three")
			elif num[1] == '4':
				wordlist.append("four")
			elif num[1] == '5':
				wordlist.append("five")
			elif num[1] == '6':
				wordlist.append("six")
			elif num[1] == '7':
				wordlist.append("seven")
			elif num[1] == '8':
				wordlist.append("eight")
			elif num[1] == '9':
				wordlist.append("nine")
		else:
			if num[0] == '1' and num[1] == '0':
				wordlist.append("ten")
			if num[1] == '1':
				wordlist.append("eleven")
			elif num[1] == '2':
				wordlist.append("twelve")
			elif num[1] == '3':
				wordlist.append("thirteen")
			elif num[1] == '4':
				wordlist.append("fourteen")
			elif num[1] == '5':
				wordlist.append("fifteen")
			elif num[1] == '6':
				wordlist.append("sixteen")
			elif num[1] == '7':
				wordlist.append("seventeen")
			elif num[1] == '8':
				wordlist.append("eighteen")
			elif num[1] == '9':
				wordlist.append("nineteen")
		#print "At step len=2 num = " + str(num)
	if len(num) == 1:
		if num[0] == '0':
			wordlist.append("zero")
		elif num[0] == '1':
			wordlist.append("one")
		elif num[0] == '2':
			wordlist.append("two")
		elif num[0] == '3':
			wordlist.append("three")
		elif num[0] == '4':
			wordlist.append("four")
		elif num[0] == '5':
			wordlist.append("five")
		elif num[0] == '6':
			wordlist.append("six")
		elif num[0] == '7':
			wordlist.append("seven")
		elif num[0] == '8':
			wordlist.append("eight")
		elif num[0] == '9':
			wordlist.append("nine")
		#print "At step len=1 num = " + str(num)
	print wordlist
	return wordlist

testnum = input("How high do you want to test? (1000 max)")

charcount = 0
for i in xrange(1,testnum+1):
	wordsout = number_to_words(i)
	output = ""
	for word in wordsout:
		output += word
#str(number_to_words(testnum)[0])+str(number_to_words(testnum)[1])+str(number_to_words(testnum)[2])+str(number_to_words(testnum)[3])
	print "output starts here :" + output + " is " + str(len(output)) + " characters."
	charcount += len(output)
print "The sum of characters from 1 to " + str(testnum) + " is " + str(charcount)