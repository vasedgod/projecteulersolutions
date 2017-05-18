def fibonacci(n):
    """Calculate the nth Fibonacci number"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

evensum = 0

for x in range(50):
    fib = fibonacci(x)
    if fib <= 4000000 and fib % 2 == 0:
        evensum += fib
    if fib > 4000000:
        break

print "sum of even-valued terms <= 4,000,000: " + str(evensum)
