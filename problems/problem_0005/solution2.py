from sympy import sieve
from math import sqrt, log, floor


def smallest_multiple(n=20):
    # Returns a list of all primes <= n
    primes = sieve.primerange(n + 1)
    sqrt_n, log_n = sqrt(n), log(n)
    res = 1
    for p in primes:
        if p < sqrt_n:
            res *= p**(floor(log_n / log(p)))
        else:
            res *= p
    return res


if __name__ == "__main__":
    print(smallest_multiple())
