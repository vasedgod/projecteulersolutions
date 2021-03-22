from tools import decimal_to_binary as binary


def is_palindrome(num):
    return str(num) == str(num)[::-1]


total = 0

for num in range(1000000):
    if is_palindrome(num) and is_palindrome(binary(num)):
        total += num

print(total)
