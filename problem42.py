# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1)
# so the first ten triangle numbers are:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# By converting each letter in a word to a number corresponding to its alphabetical position
# and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
# If the word value is a triangle number then we shall call the word a triangle word.

# Using words.txt(right click and 'Save Link/Target As...'), a 16K text file containing
# nearly two-thousand common English words, how many are triangle words?

all_words = []
with open('p042_words.txt') as words_file:
    for word in words_file.readline().split(','):
        all_words.append(word[1:-1])


def word_value(word):
    """
    Return alphabetical sum of each letter in the input word
    Ex: SKY is 19 + 11 + 25 = 55
    """
    value = sum([ord(letter)-64 for letter in word])
    return value


def get_nth_triangle_num(n):
    return n * (n+1) / 2


trianglenums = []


def is_triangle_num(num):
    """
    Gets the word value for a word, then determines if it is a triangular number by
    checking if the number has already been calculated, and if not, calculates triangle numbers less than
    or equal to the number under test. If the last one checked is not equal to the number under test,
    it is not a triangle number.
    """
    global trianglenums
    if num not in trianglenums:
        n = len(trianglenums) + 1
        this_triangle_num = 0
        while this_triangle_num <= num:
            if this_triangle_num == num:
                return True
            else:
                this_triangle_num = get_nth_triangle_num(n)
                trianglenums.append(this_triangle_num)
                n += 1
        return False
    else:
        return True


# Should print 55
# print(word_value('SKY'))
# Should print True
# print(is_triangle_num(word_value('SKY')))

trianglewordcount = sum([is_triangle_num(word_value(word))
                         for word in all_words])
print(trianglewordcount)
