def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n-2) + fib(n-1)


def memo(f):
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized

fib = memo(fib)

digitcount = input("First fibonacci number to have how many digits? ")

i = 2

while len(list(str(fib(i)))) < digitcount:
    p#rint str(fib(i)) + " has " + str(len(str(fib(i)))) + " digits."
    i += 1

print "The first Fibonacci number to have " + str(digitcount) + " digits is Fibonacci number " + str(i-1) + "."