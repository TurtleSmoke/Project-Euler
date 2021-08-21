from scipy.special import lambertw
from math import exp, ceil
from sympy import sieve
from itertools import islice


def n_th_prime(n=10001):
    if n < 3:
        return [2, 3][n - 1]

    limit_pi_1 = ceil(exp(-lambertw(-1 / n, -1).real))
    primes = sieve.primerange(limit_pi_1 + 1)

    return next(islice(primes, n - 1, n))


if __name__ == "__main__":
    print(n_th_prime())
