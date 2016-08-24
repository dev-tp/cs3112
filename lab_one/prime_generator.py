# def prime_factors(n):
#     i = 2
#     factors = []
#     while i * i <= n:
#         if n % i:
#             i += 1
#         else:
#             n //= i
#             factors.append(i)
#     if n > 1:
#         factors.append(n)
#     return factors

# print prime_factors(35)

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
    # print "if n = 3: " + str(list_a_number_of_primes(3))
    # print "if n = 7: " + str(list_a_number_of_primes(7))
    print "if n = 25: " + str(list_a_number_of_primes(25))


if __name__ == "__main__":
    main()