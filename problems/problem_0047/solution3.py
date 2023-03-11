import itertools


def factors_sieves(n):
    factors = [0] * (n + 1)
    consecutive = 0
    for i in range(2, n + 1):
        if factors[i] == 0:
            for j in range(2, int(n / i)):
                factors[i * j] += 1
            consecutive = 0
        elif factors[i] == 4:
            consecutive += 1
        else:
            consecutive = 0

        if consecutive == 4:
            return i - 3
    return None


def distinct_primes_factors():
    for i in itertools.count(1):
        res = factors_sieves(2**i)
        if res is not None:
            return res


if __name__ == "__main__":
    print(distinct_primes_factors())
