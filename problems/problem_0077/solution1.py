from sympy import sieve


def prime_summations(n=100):
    numbers = list(sieve.primerange(1, n + 1))
    cache = [1] + [0] * n

    for number in numbers:
        for i in range(number, n + 1):
            cache[i] += cache[i - number]

    return next(i for i, x in enumerate(cache) if x > 5000)


if __name__ == "__main__":
    print(prime_summations())
