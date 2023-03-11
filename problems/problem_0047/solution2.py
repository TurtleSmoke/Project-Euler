import itertools

from sympy import primefactors


def distinct_primes_factors():
    cache = [False] * 4
    for i in itertools.count(1):
        cache[i % 4] = len(set(primefactors(i))) == 4
        if all(cache):
            return i - 3


if __name__ == "__main__":
    print(distinct_primes_factors())
