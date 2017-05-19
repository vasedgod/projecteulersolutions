"""Find the largest palindrome made from the product of two 3-digit numbers."""

palindromes = []
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        if str(i * j) == str(i * j)[::-1]:
            palindromes.append(i * j)
print "The largest palindrome that can be made from \
    the product of two 3-digit numbers is " + str(max(palindromes))
