import itertools

from sympy import primefactors


def distinct_primes_factors():
    for i in itertools.count(5):
        if (
            len(set(primefactors(i)))
            == len(set(primefactors(i + 1)))
            == len(set(primefactors(i + 2)))
            == len(set(primefactors(i + 3)))
            == 4
        ):
            return i


if __name__ == "__main__":
    print(distinct_primes_factors())
