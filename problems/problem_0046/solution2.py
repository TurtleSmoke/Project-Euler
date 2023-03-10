import itertools

from sympy import isprime


def is_odd_goldbach(n, primes_cache):
    if isprime(n):
        primes_cache.add(n)
        return True

    return any(n - 2 * i**2 in primes_cache for i in range(1, int(n**0.5) + 1))


def goldbachs_other_conjecture():
    primes_cache = {2, 3, 5}
    for i in itertools.count(7, 2):
        if not is_odd_goldbach(i, primes_cache):
            return i


if __name__ == "__main__":
    print(goldbachs_other_conjecture())
