def letter_to_index(letter):
    _alphabet = 'ABCEDFGHIJKLMNOPQRSTUVWXYZ'
    return next((i+1 for i, _letter in enumerate(_alphabet) if _letter == letter), None)

def word_value(word):
	value = 0
	for letter in word:
		if letter in 'ABCEDFGHIJKLMNOPQRSTUVWXYZ':
			value += letter_to_index(letter)
	return value
names_file = open("./p022_names.txt","r")
line_num = 1
running_total = 0
for line in names_file:
	print line + " value is " + str(word_value(line)) + " times " + str(line_num)
	print "for a total of " + str(word_value(line) * line_num)
	running_total += word_value(line) * line_num
	line_num += 1
print "The total name score of this list is " + str(running_total)