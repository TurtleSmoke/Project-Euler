import bisect
from itertools import accumulate

from sympy import sieve


def consecutive_prime_sum(lim=10**6):
    primes = list(sieve.primerange(2, lim))
    primes_set = set(primes)
    cumul_sum = list(accumulate(primes))
    max_window = bisect.bisect_left(cumul_sum, lim)
    for window in range(max_window, 0, -1):
        for i in range(len(cumul_sum) - window):
            s = cumul_sum[i + window] - cumul_sum[i]
            if s >= lim:
                break
            if s in primes_set:
                return s


if __name__ == "__main__":
    print(consecutive_prime_sum())
