def prime_generator():
    d = {}
    q = 2

    while True:
        if q not in d:
            yield q
            d[q * q] = [q]
        else:
            for p in d[q]:
                d[p + q] = [p]
            del d[q]
        q += 1


def list_a_number_of_primes(n):
    prime = prime_generator()
    return [next(prime) for i in range(n)]


def main():
    print "Method one:"
    print "if n = 25: " + str(list_a_number_of_primes(25))


if __name__ == "__main__":
    main()