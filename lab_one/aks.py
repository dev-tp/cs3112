# https://rosettacode.org/wiki/AKS_test_for_primes

# O(n^k)
def expand_x_one(p):
    a = [1]
    for i in range(p):
        a.append(a[-1] * -(p - i) / (i + 1))
    #     print str(i) + ": " + str(a)
    # print "Result: " + str(a[::-1])
    return a[::-1]
 

def aks_test(p):
    if p < 2:
        return False
    ex = expand_x_one(p)
    ex[0] += 1
    # print str(ex[0:-1])
    # print str([mult % p for mult in ex[0:-1]])
    return not any(mult % p for mult in ex[0:-1])


print [i for i in range(1000) if aks_test(i)]