#!/usr/bin/python
# -*- coding: utf-8 -*-


from math import sqrt
import sys


def question_one(n):  # Sieve
    d = {}
    q = 2

    i = 0
    result = []
    while i < n:
        if q not in d:
            # print "if true, d = " + str(d)
            result.append(q)
            d[q * q] = [q]
            i += 1
        else:
            # print "else case: q = " + str(q)
            for p in d[q]:
                # print "d[q]: " + str(d[q]) + ", p + q: " + str(p + q)
                d.setdefault(p + q, []).append(p)
            del d[q]
        q += 1

    return result


def question_two(n):
    return [i for i in range(n) if is_prime(i)]


def is_prime(n):  # Trial Division
    if n > 1:
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(sqrt(n) + 1), 2):
            if n % i == 0:
                return False
        return True
    return False


def question_three(n):
    i = 2
    factors = []

    while i * i <= n:
        if n % i != 0:
            i += 1
        else:
            n /= i
            factors.append(i)

    if n > 1:
        factors.append(n)

    factor_count = {}
    for i in factors:
        if i not in factor_count:
            factor_count[i] = 1
        else:
            factor_count[i] += 1
    del factors

    output = ""
    for k, v in factor_count.items():
        if (k, v) != factor_count.items()[-1]:
            output = output + "%d^%d * " % (k, v)
        else:
            output = output + "%d^%d" % (k, v)
    del factor_count

    return output


def main():
    print "Question One: if n = 3; " + str(question_one(3))
    print "Question One: if n = 7; " + str(question_one(7)) + "\n"

    print "Question Two: if n = 10; " + str(question_two(10))
    print "Question Two: if n = 16; " + str(question_two(16)) + "\n"

    print "Question Three: if n = 8; " + str(question_three(8))
    print "Question Three: if n = 72; " + str(question_three(72))


if __name__ == "__main__":
    main()