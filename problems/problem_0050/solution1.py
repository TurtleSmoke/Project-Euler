from sympy import sieve


def consecutive_prime_sum(lim=10**6):
    primes = list(sieve.primerange(2, lim))
    res = 0
    max_len = 0
    for i in range(len(primes)):
        for j in range(i + max_len, len(primes)):
            s = sum(primes[i:j])
            if s >= lim:
                break
            if j - i > max_len and s in primes:
                max_len = j - i
                res = s
    return res


if __name__ == "__main__":
    print(consecutive_prime_sum())
