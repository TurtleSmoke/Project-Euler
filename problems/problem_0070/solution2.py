from sympy import sieve


def totient_permutation(limit=10000001):
    primes = list(sieve.primerange(2, 2 * int(limit**0.5)))
    res = 0
    ratio = float("inf")
    for i in range(len(primes)):
        for j in range(i):
            if (primes[i] + primes[j] - 1) % 9 != 0:
                continue
            n = primes[i] * primes[j]
            if n > limit:
                break
            t = (primes[i] - 1) * (primes[j] - 1)
            if n / t < ratio and sorted(str(n)) == sorted(str(t)):
                res = n
                ratio = n / t
    return res


if __name__ == "__main__":
    print(totient_permutation())
