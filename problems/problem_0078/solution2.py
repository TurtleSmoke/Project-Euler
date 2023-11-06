import itertools


def p(n, cache={}):
    if n in cache:
        return cache[n]
    if n < 0:
        return 0
    if n < 2:
        return 1

    cum_sum = 0
    for k in range(1, n + 1):
        n1 = n - k * (3 * k - 1) // 2
        n2 = n - k * (3 * k + 1) // 2
        cum_sum += (-1) ** (k + 1) * (p(n1, cache) + p(n2, cache))
        if n1 <= 0:  # n1 < n2, no need to check both
            break

    cache[n] = cum_sum % 1000000
    return cache[n]


def coin_partitions(n=1000000):
    for i in itertools.count(0):
        r = p(i)
        if r % n == 0:
            return i


if __name__ == "__main__":
    print(coin_partitions())
