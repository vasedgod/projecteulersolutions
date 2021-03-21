#!/bin/env python
# It was proposed by Christian Goldbach that every odd composite number can be
# written as the sum of a prime and twice a square.
# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2

# It turns out that the conjecture was false.

# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

from tools import eratosthenes, is_prime


def square():
    num = 1
    while True:
        yield num ** 2
        num += 1


def get_decreasing_primes_less_than(val):
    prime = eratosthenes()
    primes_ascending = []

    while True:
        this_prime = next(prime)
        if this_prime < val:
            primes_ascending.append(this_prime)
        else:
            primes_descending = primes_ascending[::-1]
            return primes_descending


def conjecture_passes_for(composite_num, prime, square):
    return composite_num == prime + 2 * square


def get_squares_less_than(num):
    global square
    squares = []
    square_gen = square()
    for _ in range(0, num):
        sq = next(square_gen)
        if sq < num:
            squares.append(sq)
    return squares


def find_first_exception_to_conjecture():
    finished = False
    num = 5

    successes = {}
    while True:
        num += 2
        while is_prime(num):
            # print(num, "was prime, added 2 to get", num + 2)
            num += 2
        composite_num = num
        # print('composite_num:', composite_num)
        satisfied_conjecture = False
        successes[composite_num] = []
        primes = get_decreasing_primes_less_than(composite_num)
        for test_prime in primes:
            diff = composite_num - test_prime

            for test_square in get_squares_less_than(diff):
                # print('Squares < {}:'.format(composite_num),
                #       get_squares_less_than(diff))
                if conjecture_passes_for(composite_num, test_prime, test_square):
                    # print(
                    #     "{} = {} + 2*{}".format(
                    #         composite_num, test_prime, test_square)
                    # )
                    successes[composite_num].append((test_prime, test_square))
                    satisfied_conjecture = True
                    break
            if satisfied_conjecture:
                break
        if not satisfied_conjecture:
            print("Failed on {}".format(composite_num))
            return
        else:
            continue
        # if not satisfied_conjecture:
        #     print("FAILED ON", composite_num)
        # else:
        #     break
    # for num, combos in successes.items():
    #     print(num, ":")
    #     for combo in combos:
    #         print("\n\tp = {}, s = {}".format(combo[0], combo[1]))


find_first_exception_to_conjecture()
