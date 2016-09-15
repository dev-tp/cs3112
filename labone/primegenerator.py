#!/usr/bin/python
# -*- coding: utf-8 -*-


from math import sqrt


def question_one(n):  # Sieve
    d, result = {}, []
    i, q = 0, 2

    while i < n:
        if q not in d:
            result.append(q)
            d[q * q] = [q]
            i += 1
        else:
            for p in d[q]:
                if p + q in d:
                    d[p + q].append(p)
                else:
                    d[p + q] = [p]
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
    factors = {}
    i = 2

    while i * i <= n:
        if n % i != 0:
            i += 1
        else:
            n /= i
            factors[i] = 1 if i not in factors else factors[i] + 1

    if n > 1:
        factors[n] = 1 if n not in factors else factors[n] + 1

    output = ""
    for k, v in factors.items():
        if (k, v) != factors.items()[-1]:
            output = output + "%d^%d * " % (k, v)
        else:
            output = output + "%d^%d" % (k, v)

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