from sympy import isprime, sieve


def concat(p1, p2):
    return isprime(int(str(p1) + str(p2))) and isprime(int(str(p2) + str(p1)))


def prime_pair_sets():
    primes = list(sieve.primerange(10000))
    for i, p1 in enumerate(primes):
        for j, p2 in enumerate(primes[:i]):
            if any(not concat(p, p2) for p in (p1,)):
                continue
            for k, p3 in enumerate(primes[:j]):
                if any(not concat(p, p3) for p in (p1, p2)):
                    continue
                for l, p4 in enumerate(primes[:k]):
                    if any(not concat(p, p4) for p in (p1, p2, p3)):
                        continue
                    for p5 in primes[:l]:
                        if all(concat(p, p5) for p in (p1, p2, p3, p4)):
                            return p1 + p2 + p3 + p4 + p5


if __name__ == "__main__":
    print(prime_pair_sets())
